import requests
# requests.packages.urllib3.disable_warnings()
from lxml import etree
import json


def down():
    for page in range(0, 50):
        url = 'https://open.taou.com/maimai/feed/v5/nd1feed?u=228402786&access_token=1.41f7d570307601b1e66d032b332ce4a3&version=5.0.16&ver_code=android_10018&channel=Web&vc=Android%204.4.2%2F19&push_permit=1&net=wifi&open=icon&appid=3&device=vivo%20vivo%20X20A&imei=866174010542385&udid=6fd644f7-24d6-4131-af81-5ae3e449492a&is_push_open=1&isEmulator=0&density=1.5&launch_uuid=f2352824-7edd-41ec-9c33-25e099e97193&session_uuid=8074c200-46c9-4357-a200-7c0195c137ef&from_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.fragment.ExpandListFragment%26uuid%3D7ee15b1b-afbb-453f-92e3-38c37384dfb8%26url%3Dtaoumaimai%253A%252F%252Fhome%253Fhosttype%253D101&src_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.profile.view.activity.BlankActivity%26uuid%3D2035587b-e623-4c4f-bebb-53158aef3bc7&to_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.fragment.ExpandListFragment%26uuid%3D7ee15b1b-afbb-453f-92e3-38c37384dfb8%26url%3Dtaoumaimai%253A%252F%252Fhome%253Fhosttype%253D101&last_launch_time=1565319892414&action=out_date&thumb_size=404&page_tab=explore_list&page=0&pfmj_commend_cnt=0'
        # url = 'https://open.taou.com/maimai/feed/v5/nd1feed?u=228402733&access_token=1.8185ed368e274f757ddcfffd85edb0ba&version=5.0.16&ver_code=android_10018&channel=Web&vc=Android%204.4.2%2F19&push_permit=1&net=wifi&open=icon&appid=3&device=Xiaomi%20%20MI%206%20&imei=863254010228111&udid=0b724b03-2e86-4036-8a2e-aee3cde73260&is_push_open=1&isEmulator=0&density=1.5&launch_uuid=19c478fc-7739-4e13-b2e1-8c05412dcc54&session_uuid=c5ac3b00-bbe2-4678-88f5-b859d178dc1f&from_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.fragment.ExpandListFragment%26uuid%3D7610928b-9302-4994-bd1e-3f6e6f61713d%26url%3Dtaoumaimai%253A%252F%252Fhome%253Fhosttype%253D101&src_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.SplashActivity%26uuid%3Dedbd6a38-912d-410a-ab3c-f08f8ebf888d&to_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.fragment.ExpandListFragment%26uuid%3D7610928b-9302-4994-bd1e-3f6e6f61713d%26url%3Dtaoumaimai%253A%252F%252Fhome%253Fhosttype%253D101&last_launch_time=1565334807100&action=bottom_tab&thumb_size=404&page_tab=explore_list&page=0&pfmj_commend_cnt=0'
        # url = 'https://open.taou.com/maimai/gossip/v3/feed?u=228402786&access_token=1.41f7d570307601b1e66d032b332ce4a3&version=5.0.16&ver_code=android_10018&channel=Web&vc=Android%204.4.2%2F19&push_permit=1&net=wifi&open=icon&appid=3&device=vivo%20vivo%20X20A&imei=866174010542385&udid=6fd644f7-24d6-4131-af81-5ae3e449492a&is_push_open=1&isEmulator=0&density=1.5&launch_uuid=f2352824-7edd-41ec-9c33-25e099e97193&session_uuid=7f351044-0bb1-44d9-8684-cfda4f2c258d&from_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.gossip.fragment.GossipFragmentRefactor%26uuid%3D03dd3635-fe1b-4d88-b858-808172c49aba&src_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.profile.view.activity.BlankActivity%26uuid%3D2035587b-e623-4c4f-bebb-53158aef3bc7&to_page=taoumaimai%3A%2F%2Fpage%3Fname%3Dcom.taou.maimai.gossip.fragment.GossipFragmentRefactor%26uuid%3D03dd3635-fe1b-4d88-b858-808172c49aba&last_launch_time=1565319892414&action=by_user&page=0'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',

        }

        response = requests.get(url, headers=headers, verify=False)
        response = json.loads(response.text)
        print(response)
        for data in response:
            # print(data)
            author = data['common']['unwills'][3]
            print(author)
            print('======')
            for each in author:
                # print(each)
                author = each['text']
            # print('author:',author)
            # title = data['style1']['text'].strip()
            # print('title:',title)


if __name__ == '__main__':
    down()
