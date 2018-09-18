from urllib import request,parse
import re
def crawl(keyword):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
        'Referer': 'https://user.zgg.com',
        'Host':'search.zgg.com',
        'Cookie':'tmpid=7ea05cdc-b189-11e8-8e09-0000df4828d3; gr_user_id=8cc525bd-267c-420b-b757-896bba96de71; gr_session_id_b34a91e0993dce4c=38eb025c-6711-4f44-992b-3e769d578684; gr_session_id_b34a91e0993dce4c_38eb025c-6711-4f44-992b-3e769d578684=true; UM_distinctid=165ad0b0b4f1f6-0149deb46e09ea-2711639-100200-165ad0b0b507d2; CNZZDATA1259629797=504348692-1536202751-%7C1536202751; NTKF_T2D_CLIENTID=guestD5750E0A-BC29-85CF-BA72-AD0B0C21191F; judgeMedia=; firstLand=; b34a91e0993dce4c_gr_session_id=c8b54b79-b19a-423c-ad6f-76053239421d; _jzqa=1.1167687049723451000.1536206508.1536206508.1536206508.1; _jzqc=1; _jzqx=1.1536206508.1536206508.1.jzqsr=search%2Ezgg%2Ecom|jzqct=/tools/search-list-zl%2Ehtml.-; _jzqckmp=1; grwng_uid=6036976c-d2b2-471c-9326-6acdb63d3f14; b34a91e0993dce4c_gr_session_id_c8b54b79-b19a-423c-ad6f-76053239421d=true; redirect=http%3A%2F%2Fwww.zgg.com%2F; Hm_lvt_0eaa3be1a1b4ffd7be2065d4c04c3a3f=1536206507,1536207516; LXB_REFER=open.weixin.qq.com; userName=18810793159; IsSelfReg=0; userID=50796; userToken=177A8B72A50346C2E598BA00D74B0BB2; nTalk_CACHE_DATA={uid:kf_9333_ISME9754_50796,tid:1536206507039129}; _jzqb=1.19.10.1536206508.1; Hm_lpvt_0eaa3be1a1b4ffd7be2065d4c04c3a3f=1536207588'
    }
    url = 'http://search.zgg.com/tools/search-list-zl.html?{}'
    keywords = parse.urlencode({'keywords':keyword})
    url = url.format(keywords)
    req = request.Request(url,headers=headers)
    response = request.urlopen(req)
    response = response.read().decode('utf-8')
    pattern = 'first-line">.*?<span class="comm">(.*?)</span>.*?secnod-line">.*?<p class="third">.*?<span title=.*?>(.*?)</span>.*?third-line">.*?<p class="first">.*?<span title=.*?>(.*?)</span>.*?four-line">.*?<span class="zk".*?"(.*?)">[查看]'
    content = re.findall(pattern,response,re.S)
    for item in content:
        yield {
            'title':item[0],
            'applicant':item[1],
            'number':item[2],
            'abstract':item[3]
        }

if __name__=='__main__':
    keyword = input('请输入关键词：')
    # keyword=str(keyword)
    for item in crawl(keyword):
        print(item)

