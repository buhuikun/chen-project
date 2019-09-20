import requests

if __name__ == '__main__':
    i = input('输入要翻译的内容。。。')
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    Form_Data = {}
    Form_Data['i'] = i
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1526796477689'
    Form_Data['sign'] = 'd0a17aa2a8b0bb831769bd9ce27d28bd'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTIME'
    Form_Data['typoResult'] = 'false'
    head = {}
    # 写入User Agent信息
    head[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'

    response = requests.post(Request_URL, data=Form_Data, headers=head)
    print(response)
    print(response.text)
    translate_results = response.json()
    # #找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    # #打印翻译信息
    print("翻译的结果是：%s" % translate_results)
