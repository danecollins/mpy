#!/usr/bin/env python

####################################################################
#                                                                  #
#         Script: DOCBOOK TO WIKI                                  #
#         Author: Pep Ribal                                        #
#         Version: 1.0                                             #
#                                                                  #
####################################################################
#                                                                  #
#         IMPORTANT                                                #
#         =========                                                #
#         LOOK FOR '%%%%%' INDICATIONS IN THE OUTPUT FILE          #
#         Set titleNote as desired (translation of "Note")         #
#         Double quotes assumed in tags (atrib="val" style)        #
#                                                                  #
####################################################################
 
#
# Recognized tags so far:
#
# chapter, section, bridgehead, orderedlist, itemizedlist,
# emphasis, literal, xref, figure, informalequation, link,
# inlinegraphic, command, tip, note, para, keycap
#
 
 
# set titleNote to the desired value in doble quotes (in English, "Note")
titleNote="Note"
 
# Advances until next '<' char; 0 - No output, 1- Output; returns tag name
def nextag(out):
	global buffer,lastChar,fout
	while len(buffer)>0 and buffer[0]!="<":
		if out==1:
			# No TABS, NLs or CRs will be written:
			if buffer[0]=="\t" or buffer[0]=="\n" or buffer[0]=="\r":
				presentChar=" "
			else:
				presentChar=buffer[0]
			if (lastChar==" " or lastChar=="\n" or lastChar=="(") and presentChar==" ":
				presentChar=""		# Avoid these combinations
			fout.write(presentChar)
			if presentChar!="":
				lastChar=presentChar
		buffer=buffer[1:]
	if buffer=="":
		return		# EOF
	tag=""
	while buffer[0]!=" " and buffer[0]!="\t" and buffer[0]!="\n" and buffer[0]!="\r" and buffer[0]!=">":
		tag=tag+buffer[0]
		buffer=buffer[1:]
	buffer=buffer[1:]
	return tag[1:]
 
# Returns string until string found (removes all from buffer)
def contentUntil(until):
	global buffer
	straux=""
	lastChar="*"		# This is not the global variable; just an internal control var
	while not buffer.startswith(until):
		# No TABS, NLs or CRs will be written:
		if buffer[0]=="\t" or buffer[0]=="\n" or buffer[0]=="\r":
			presentChar=" "
		else:
			presentChar=buffer[0]
		if (lastChar==" " or lastChar=="\n" or lastChar=="(") and presentChar==" ":
			presentChar=""		# Avoid these combinations
		straux+=presentChar
		buffer=buffer[1:]
		if presentChar!="":
			lastChar=presentChar
	buffer=buffer[len(until):]
	return straux
 
 
def xml2wiki(fname):
	global buffer,lastChar,fout
	listType="?"
	lastChar="*"
	fin=open(fname,"r")
	fout_name = fname[:-4]+".txt"
	fout=open(fname[:-4]+".txt","w")
	buffer=fin.read()
	outp=0
	while len(buffer)>0:
		aux=nextag(outp)
		if aux=="chapter":
			contentUntil("<title>")
			fout.write("\nh2. "+contentUntil("</title>")+"\n")
			lastChar="\n"
		elif aux=="info":
			contentUntil("<title>")
			fout.write("\nh1. "+contentUntil("</title>")+"\n")
			lastChar="\n"
		elif aux=="sect1":
			contentUntil("<title>")
			fout.write("\nh3. "+contentUntil("</title>")+"\n")
			lastChar="\n"
		elif aux=="bridgehead":
			contentUntil(">")
			fout.write("\n==="+contentUntil("</bridgehead>")+"===\n")
			lastChar="\n"
		elif aux=="para":
			fout.write("\n")
			lastChar="\n"
			outp=1
		elif aux=="emphasis" or aux=="/emphasis":
			fout.write("''")
			lastChar="'"
		elif aux=="guimenu" or aux=="/guimenu":
			fout.write("*")
			lastChar="*"
		elif aux=="<guilabel>":
			fout.write("*_"+contentUntil("</guilabel")+"_*")
			lastChar="*"
		elif aux=="/para":
			fout.write("\n")
			lastChar="\n"
			outp=0
		elif aux=="itemizedlist":
			fout.write("\n")
			lastChar="\n"
			listType="* "
		elif aux=="orderedlist":
			fout.write("\n")
			lastChar="\n"
			listType="# "
		elif aux=="listitem":			
			contentUntil("<para>")
			outp=1
			fout.write(listType)
			lastChar=" "
		elif aux=="keycap":
			fout.write("{{KEY|"+contentUntil("</keycap>")+"}}")
			lastChar="}"
		elif aux=="literal":
			fout.write("{{Literal|"+contentUntil("</literal>")+"}}")
			lastChar="}"
		elif aux=="xref":
			contentUntil('="')
			fout.write("''%%%%%XREF:"+contentUntil('"/>')+"''")
			lastChar="'"
		elif aux=="informalfigure":
			contentUntil('images/')
			fout.write("\n\n!"+contentUntil('"')+"|align=center!\n\n")
			lastChar="\n"
			contentUntil("</informalfigure>")
		elif aux=="inlinegraphic":
			contentUntil('="')
			fout.write("[[Image:"+contentUntil('"')+"]]")
			lastChar="]"
			contentUntil(">")
		elif aux=="command":
			fout.write("%%%%%COMMAND:")
			lastChar=":"
		elif aux=="/command":
			fout.write(":COMMAND%%%%%")
			lastChar="%"
		elif aux=="tip" or aux=="note":
			while buffer[0]!="<":		# We might want to keep the '<' char in buffer
				buffer=buffer[1:]
			if buffer[:7]=="<title>":
				buffer=buffer[7:]
				fout.write("\n{{Tip|"+contentUntil("</title>")+"|")
			else:
				fout.write("\n{{Tip|"+titleNote+"|")
			lastChar="|"
		elif aux=="/tip" or aux=="/note":
			fout.write("}}\n")
			lastChar="\n"
		elif aux=="informalequation":
			fout.write("\n%%%%%INFORMALEQUATION:")
			fout.write(contentUntil("</informalequation>"))
			fout.write(":INFORMALEQUATION%%%%%\n")
			lastChar="\n"
		elif aux=="link":
			contentUntil('="')
			fout.write("%%%%%LINK:"+contentUntil('">')+"==>"+contentUntil("</link>")+":LINK%%%%%")
			lastChar="%"
	fout.close()
	fin.close()
	## need to fix things I can't figure out how to fix in the code directly -- dmc
	fin = open(fout_name)
	str = fin.read()
	str = str.replace('&ohm','&Omega')
	fin.close()
	fout = open(fout_name,'w')
	fout.write(str)
	fout.close


def fileSel(filename):
	xml2wiki(filename)
        
xml2wiki("c:\\tmp\\d2w\\EMDC.xml")