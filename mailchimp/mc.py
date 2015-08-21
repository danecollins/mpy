from __future__ import print_function
from __future__ import unicode_literals

import os

import mailchimp


class LeadActivity:
    @classmethod
    def get(cls, email_address):
        self = cls()
        self.email = email_address
        apikey = os.environ.get('MAILCHIMP_API_AWR')
        master_list = '1090921d49'
        campaigns = set()
        opens = set()
        clicks = set()
        mc = mailchimp.Mailchimp(apikey=apikey)
        email_array = [{'email': email_address}]
        result = mc.lists.member_activity(master_list, email_array)
        for action in result['data'][0]['activity']:
            action_type = action['action']
            id = action['campaign_id']
            # timestamp = action['timestamp']
            # name = action['campaign_data']['subject']
            if action_type == 'sent':
                campaigns.add(id)
            elif action_type == 'open':
                opens.add(id)
            elif action_type == 'click':
                clicks.add(id)
            else:
                print('Unknown action type = "{}"'.format(action_type))

        self.campaigns = len(campaigns)
        self.opens = len(opens)
        self.clicks = len(clicks)
        return self

    def __str__(self):
        return "LeadActivity({},C={},O={},C={})".format(self.email, self.campaigns,
                                                        self.opens, self.clicks)

if __name__ == '__main__':
    x = LeadActivity.get('jerome.rossignol@u-bourgogne.fr')
    print(x)