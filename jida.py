import requests

headers = {
    'Host': 'service-yy.jconnect.faw-vw.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; EBG-AN10 Build/HUAWEIEBG-AN10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36',
    'token': 'Bearer eyJraWQiOiJmNGVkOGEyYS1jMjI0LTRlZTQtYjhhYi0xNGViNTk2NzdjOTEiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2lkcC5tb3NjLmZhdy12dy5jb20iLCJhbXIiOiJwd2QiLCJ0eXBlIjoiQVQiLCJhenAiOiJBUFAiLCJhdWQiOlsiVldHTUJCMDFDTkxJVjEiLCJhdXRvbmF2aS5jb20iLCIyMENFM0Q4RjlERUU1NEMzNjM5RjdGODgwMjcyMjZFNyJdLCJzdWIiOiIxMzA4OTgwOCIsImlhdCI6MTY2MTQyODA5NiwidmVyIjoiMC4wLjEiLCJ0eXAiOiJSVCIsImNjaCI6IkFQUCIsImV4cCI6MTY2MTcyODA5NiwianRpIjoiMWU4MTVkMjQtZmU0Ni00MjllLTlhOWEtNTA1YmYyOWRkNzMwIiwiaWR0LWlkIjoiYjhlZjk5OTctODA3ZS00YTI3LTgyZTYtZDM5YmI4NzEyNWU3IiwiY29yIjoiQ04iLCJzY3AiOiJvcGVuaWQgcHJvZmlsZSBtYmIiLCJhaWQiOiIxMzA4OTgwOCIsInRudCI6IkVCT19BUFBfSE9OT1ItRUJHLUFOMTBfMjBDRTNEOEY5REVFNTRDMzYzOUY3Rjg4MDI3MjI2RTdfQW5kcm9pZDEwX3YyLjMuMTYiLCJydC1pZCI6ImYyMjQ1ZWIwLWJkYTctNDliZC1hMzc3LTc2NTA5MDRmY2FiMyJ9.LlbU9vz3qi7KyoPaUzlsYFN-8sBNHt2CGM5mgqwnDvj6EgCDF6OQFnh3YVX5TzjXUdrm6P-VqnPd4WUMVq6NOEFLZN53DaBT5B0MQIrvwWQNV3rFc-2eOM4QFwjQjgc8ReUa2gx0jz8MfJ10qevzs5wiwJVOs9dVAk7_TurlZ-Y-0fY72ZQJdbpH1BexU2yzBnwdoJ4nPLljf4Ds-vr2mZ0KtHy4LNh1qnrSdkCR8OplJ7b_C3h4E9knqTq2j2DIuPFTt97e7qDwqNc83cJcR7n3DkQDCp7UgVsX9-0qUNg60p-h6SBwrlnrnGyORDf46cPmKRtWQGp9__-656VjVA',
    'origin': 'https://serviceui-yy-ui.jconnect.faw-vw.com',
    'x-requested-with': 'com.fawvw.ebo',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://serviceui-yy-ui.jconnect.faw-vw.com/service-activity/20220517/dist/',
    # 'accept-encoding': 'gzip, deflate',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
}

response = requests.get('https://service-yy.jconnect.faw-vw.com/redpackbank/prize/getPrize', headers=headers)