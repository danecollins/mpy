from html_utils import gen_html_page

values = {'SECURED_ITEMS' : '<item>1</item>',
		  'UNSECURED_ITEMS': '<item>2</item>'}
print gen_html_page('html/setup.stub.html', values)