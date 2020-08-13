### 咪咕音乐

#### web端（未完成）

* 函数参数

``` javascript
t = {
    rawType: 2
    raw: {
        copyrightId: "6005661F31N" // 每首歌曲的唯一版权id
        type: 1 // 歌曲的音质：1，2（超清），3（无损）
        auditionsFlag: 0
    }
}
```

* 歌曲下载请求url：【get】https://music.migu.cn/v3/api/music/audioPlayer/getPlayInfo

* 歌词请求url：【get】https://music.migu.cn/v3/api/music/audioPlayer/getLyric?copyrightId=6005661F31N （copyrightId为歌曲唯一版权id）

* 歌曲图片url：【get】https://music.migu.cn/v3/api/music/audioPlayer/getSongPic?songId=1106588664 （songid为歌曲唯一标识id）

* 歌曲下载params参数：

``` 
dataType: 2
data: 加密
secKey: 加密
```

* 响应内容：

``` 
{
    returnCode: "000000"
    msg: "成功"
    data: {
        playUrl: "//freetyst.nf.migu.cn/public/product5th/product35/2019/12/0410/2018年12月18日15点55分批量项目正东100首-15/歌曲下载/MP3_40_16_Stero/6005661F31N.mp3?key=67797b22319e2000&Tim=1597143646489&channelid=00&msisdn=3919fa715dca40f7b325f7d4216423e3&CI=6005661F31N2600914000005453273&F=000009"
        formatId: "000009"
        salePrice: ""
        bizType: "00"
        bizCode: ""
        auditionsLength: 0
    }
}
```

#### mobile端

**有时候web很难破解，此时可以尝试mobile端,但是mobile端很多时候是会数据不全，比如咪咕音乐就没有音质选择，没有无损，3D环绕等url**

* 搜索请求url：https://m.music.migu.cn/migu/remoting/scr_search_tag?rows=10&type=2&keyword=周杰伦&pgc=5

   + rows：每页展示歌曲数目
   + keyword：搜索关键词
   + pgc：页码

* 搜索url返回结果

``` json
{
    "musics":[
        {
            "albumName":"周杰伦的床边故事",
            "albumId":"1003767159",
            "copyrightId":"60054704037",
            "mp3":"https://freetyst.nf.migu.cn/public%2Fproduct8th%2Fproduct39%2F2020%2F04%2F2415%2F2016%E5%B9%B408%E6%9C%8815%E6%97%A509%E7%82%B919%E5%88%86%E5%86%85%E5%AE%B9%E5%87%86%E5%85%A5%E7%BA%B5%E6%A8%AA%E4%B8%96%E4%BB%A310%E9%A6%96%2F%E5%85%A8%E6%9B%B2%E8%AF%95%E5%90%AC%2FMp3_64_22_16%2F60054704037153557.mp3",
            "unuseFlag":null,
            "songName":"告白气球",
            "mvId":"",
            "lyrics":"http://218.200.230.40:18089/files/lyric/2019-02-12/a6da690fd12c4ef786a0624d56e0f24f.lrc",
            "mvCopyrightId":null,
            "id":"1004202180",
            "singerId":"112",
            "title":"告白气球",
            "cover":"https://mcontent.migu.cn/newlv2/new/album/20191031/1003767159/s_ZhUIXzWDPTFvv8dN.jpg",
            "hasMv":null,
            "singerName":"周杰伦",
            "isHdCrbt":null,
            "hasSQqq":"1",
            "artist":"周杰伦",
            "hasHQqq":"1"
        },
        {
            "albumName":"十一月的萧邦",
            "albumId":"8591",
            "copyrightId":"60054701952",
            "mp3":"https://freetyst.nf.migu.cn/public%2Fproduct8th%2Fproduct39%2F2020%2F04%2F2414%2F2009%E5%B9%B406%E6%9C%8826%E6%97%A5%E5%8D%9A%E5%B0%94%E6%99%AE%E6%96%AF%2F%E5%85%A8%E6%9B%B2%E8%AF%95%E5%90%AC%2FMp3_64_22_16%2F60054701952142414.mp3",
            "unuseFlag":null,
            "songName":"枫",
            "mvId":"",
            "lyrics":"http://218.200.230.40:18089/files/lyric/2020-04-24/3505b50b4c104fe5b1faf15dcf24fb7f.lrc",
            "mvCopyrightId":"600570Y9BMC",
            "id":"4148",
            "singerId":"112",
            "title":"枫",
            "cover":"https://mcontent.migu.cn/newlv2/new/album/20191125/8591/s_KV3amA6En4HiVOkO.jpg",
            "hasMv":"1",
            "singerName":"周杰伦",
            "isHdCrbt":null,
            "hasSQqq":"1",
            "artist":"周杰伦",
            "hasHQqq":"1"
        }
    ],
    "pgt":261,
    "keyword":"周杰伦",
    "pageNo":"5",
    "success":true
}
```

+ 歌曲详细页API1：https://m.music.migu.cn/migu/remoting/cms_detail_tag?cpid={版权id即copyrightId}

```json
{
    "data":{
        "auditions":null,
        "auditionsFlag":null,
        "copyrightId":"60054701962",
        "cr":{
            "copyrihtId":"600547019620",
            "invalidateDate":"2022-11-30",
            "productId":"600902000006889204",
            "resourceIdList":[

            ],
            "validateDate":null
        },
    "customizedPicUrl":null,
    "fanyiLrc":null,
    "has24Bitqq":null,
    "has3Dqq":null,
    "hasHQqq":"1",
    "hasMv":"1",
    "hasSQqq":"1",
    "isHdCrbt":null,
    "lift":null,
    "lisCr":"https://freetyst.nf.migu.cn/public%2Fproduct5th%2Fproduct35%2F2019%2F11%2F1816%2F2009%E5%B9%B406%E6%9C%8826%E6%97%A5%E5%8D%9A%E5%B0%94%E6%99%AE%E6%96%AF%2F%E5%BD%A9%E9%93%83%2F6_mp3-128kbps%2F60054701962.mp3",
    "lisQq":null,
    "listenUrl":"https://freetyst.nf.migu.cn/public%2Fproduct5th%2Fproduct35%2F2019%2F11%2F1816%2F2009%E5%B9%B406%E6%9C%8826%E6%97%A5%E5%8D%9A%E5%B0%94%E6%99%AE%E6%96%AF%2F%E5%85%A8%E6%9B%B2%E8%AF%95%E5%90%AC%2FMp3_64_22_16%2F60054701962.mp3",
    "lyricLrc":"[00:00.10]歌曲名 听妈妈的话
                [00:00.20]歌手名 周杰伦
                [00:00.30]作词：周杰伦
                [00:00.40]作曲：周杰伦
                ......
                [04:07.97]天使的魔法温暖中慈祥
                ",
    "mvCopyrightId":"600570Y6989",
    "picL":"https://mcontent.migu.cn/newlv2/new/album/20200313/7952/l_zg1XXTJxPOLC00r5.jpg",
    "picM":"https://mcontent.migu.cn/newlv2/new/album/20200313/7952/m_BiRmcpUCK4n7ye4H.jpg",
    "picS":"https://mcontent.migu.cn/newlv2/new/album/20200313/7952/s_xOuYdbY0cQGq9YY8.jpg",
    "qq":{
        "copyrihtId":"600547019622",
        "invalidateDate":"2022-11-30",
        "productId":"600902000006889206",
        "resourceIdList":[
            "011001",
            "011002",
            "000009",
            "020010",
            "020026",
            "020007",
            "020025",
            "011003",
            "020024"
        ],
        "validateDate":"2009-06-30"
    },
    "relationTitle":null,
    "rt":{
        "copyrihtId":"600547019621",
        "invalidateDate":"2022-11-30",
        "productId":"600902000006889205",
        "resourceIdList":[
            "000018",
            "010014",
            "999992",
            "999993"
        ],
        "validateDate":"2009-06-29"
    },
    "singerId":[
        "112"
    ],
    "singerName":[
        "周杰伦"
    ],
    "songDesc":null,
    "songId":"9925",
    "songName":"听妈妈的话",
    "unuseFlag":null
    }
}
```

PS:返回的json数据中，就有`歌词url` ,`播放url`,但都不是高清，无损的。想要获取高清，无损的音质，就需要接下来的API2勒


+ 歌曲播放的API2：https://app.pd.nf.migu.cn/MIGUM3.0/v1.0/content/sub/listenSong.do?channel=mx&copyrightId={copyrightId}&contentId={contentId}&toneFlag={toneFlag}&resourceType={resourceType}netType=00

   - 参数说明：
   
      - copyrightId：每一首歌的唯一版权号
      - contentId：每一首歌的唯一的内容好，其实是https://m.music.migu.cn/migu/remoting/cms_detail_tag?cpid={版权id即copyrightId} 的json返回值的["qq"]下的["productId"]
      - toneFlag：音质：LQ,HQ,SQ,3D,24Bit（音质的选择是根据API1来判断的）
      - resourceType:固定值2
