## pixiv

- [x] 解析api接口
   - [x] 搜索
   - [x] 排行榜
   - [x] 获取目标画师的作品集
   

### 1. 搜索

+ method：get

+ api：

https://www.pixiv.net/ajax/search/artworks/{搜索关键词}

+ params：

```json
params = {
    "order":"",
    "p":"",
    "s_mode":"",
    "type":"",
    "lang":"",
}

```
params含义：

| 字段 | 类型 | 必要性 | 描述 | 备注 |
|:-----:|:----:|:----:|:---:|:---:|
| order | String | Y | 排序 | 按最新排列：date_d,按旧排序：date,按热门度排序（仅会员）|
| mode | String | Y | 类别 | 全部：all,全年龄：safe,R-18：r18 |
| p | Integer | Y | 页码 | 起始页为1 |
| s_mode | String | N | 标签 | 标签(完全一致)：s_tag_full,标签(部分一致)：s_tag,标题及说明文字：s_tc |
| type | String | N | 分类 | 插画：illust_and_ugoira,漫画：manga |
| lang | String | N | 关键词语言类型 | 中文：zh |

+ 返回值：

```json
{
    "error":false,
    "body":{
        "illustManga":{
            "data":[
                {
                    "id":"86028397",
                    "title":"Kda Evelynn",
                    "illustType":0,
                    "xRestrict":0,
                    "restrict":0,
                    "sl":2,
                    "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/12/01/18/02/48/86028397_p0_square1200.jpg",
                    "description":"",
                    "tags":[
                        "KDAEvelynn",
                        "KDA",
                        "Evelynn(K/DA)",
                        "Evelynn"
                    ],
                    "userId":"19454662",
                    "userName":"Maninova",
                    "width":724,
                    "height":1024,
                    "pageCount":1,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#KDAEvelynn Kda Evelynn - Maninova的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2020-12-01T18:02:48+09:00",
                    "updateDate":"2020-12-01T18:02:48+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2016/09/25/01/46/05/11538324_81d465ea66cab126a6e1f61e0d443ee9_50.jpg"
                },
                {
                    "id":"86027348",
                    "title":"Seraphine After The Concert ♪",
                    "illustType":0,
                    "xRestrict":1,
                    "restrict":0,
                    "sl":6,
                    "url":"https://i.pximg.net/c/250x250_80_a2/custom-thumb/img/2020/12/01/16/59/48/86027348_p0_custom1200.jpg",
                    "description":"",
                    "tags":[
                        "R-18",
                        "fanart",
                        "Seraphine(KDA)",
                        "teemo",
                        "LOL",
                        "League_of_Legends",
                        "Leagueoflegends",
                        "KDA",
                        "リーグ・オブ・レジェンド"
                    ],
                    "userId":"13885928",
                    "userName":"FKS CrashinG",
                    "width":2894,
                    "height":4478,
                    "pageCount":5,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#fanart Seraphine After The Concert ♪ - FKS CrashinG的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2020-12-01T16:59:48+09:00",
                    "updateDate":"2020-12-01T16:59:48+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2020/01/12/04/11/03/16839575_d940584612068f5cf043f99e427330aa_50.png"
                },
                {
                    "id":"86023100",
                    "title":"K/DA Akali",
                    "illustType":0,
                    "xRestrict":1,
                    "restrict":0,
                    "sl":6,
                    "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/12/01/10/42/43/86023100_p0_square1200.jpg",
                    "description":"",
                    "tags":[
                        "R-18",
                        "League_of_Legends",
                        "akali",
                        "kda",
                        "女の子",
                        "魅惑のふともも",
                        "アカリ",
                        "英雄联盟",
                        "K/DA",
                        "おっぱい"
                    ],
                    "userId":"55190835",
                    "userName":"Eerisyn",
                    "width":862,
                    "height":1100,
                    "pageCount":2,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#League_of_Legends K/DA Akali - Eerisyn的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2020-12-01T10:42:43+09:00",
                    "updateDate":"2020-12-01T10:42:43+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2020/10/17/14/06/41/19523488_e66bc95fb588a8b77a24811696fb872a_50.jpg"
                },
                {
                    "id":"86020757",
                    "title":"Fanart K/DA - Ahri (All Out)",
                    "illustType":0,
                    "xRestrict":0,
                    "restrict":0,
                    "sl":4,
                    "url":"https://i.pximg.net/c/250x250_80_a2/custom-thumb/img/2020/12/01/05/44/11/86020757_p0_custom1200.jpg",
                    "description":"",
                    "tags":[
                        "fantasy",
                        "女の子",
                        "girl",
                        "fanart",
                        "kda",
                        "ahri",
                        "allout",
                        "女性",
                        "leagueoflegends",
                        "lol"
                    ],
                    "userId":"30069083",
                    "userName":"MyArtriO",
                    "width":2451,
                    "height":3429,
                    "pageCount":2,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#fantasy Fanart K/DA - Ahri (All Out) - MyArtriO的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2020-12-01T05:44:11+09:00",
                    "updateDate":"2020-12-01T05:44:11+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2020/08/10/20/59/32/19153308_be2fff8270ec43822f7ebd8cc843e391_50.jpg"
                },
                {
                    "id":"86013122",
                    "title":"K/DA",
                    "illustType":0,
                    "xRestrict":1,
                    "restrict":0,
                    "sl":6,
                    "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/11/30/22/29/08/86013122_p0_square1200.jpg",
                    "description":"",
                    "tags":[
                        "R-18",
                        "LOL",
                        "League_of_Legends",
                        "英雄联盟",
                        "Ahri",
                        "Kaisa",
                        "Akali",
                        "Evelynn",
                        "K/DA",
                        "KDA"
                    ],
                    "userId":"34144277",
                    "userName":"ROKE",
                    "width":1920,
                    "height":1080,
                    "pageCount":1,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#LOL K/DA - ROKE的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2020-11-30T22:29:08+09:00",
                    "updateDate":"2020-11-30T22:29:08+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2018/11/13/09/25/24/15010007_989e47d0631133ca9b2d3c17e16d9768_50.jpg"
                },
                {
                    "id":"85992188",
                    "title":"伊芺琳",
                    "illustType":0,
                    "xRestrict":0,
                    "restrict":0,
                    "sl":6,
                    "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/11/29/22/36/14/85992188_p0_square1200.jpg",
                    "description":"",
                    "tags":[
                        "伊芙琳",
                        "寡妇",
                        "KDA",
                        "英雄联盟",
                        "LOL"
                    ],
                    "userId":"59260886",
                    "userName":"夜玲风",
                    "width":960,
                    "height":540,
                    "pageCount":1,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#伊芙琳 伊芺琳 - 夜玲风的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2020-11-29T22:36:14+09:00",
                    "updateDate":"2020-11-29T22:36:14+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2020/11/17/00/16/51/19680773_a95335dd73adf8cdcc88bc91ae86bceb_50.jpg"
                }
            ],
            "permanent":[
                {
                    "id":"84068311",
                    "title":"K/DA Ahri",
                    "illustType":0,
                    "xRestrict":0,
                    "restrict":0,
                    "sl":2,
                    "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/08/31/21/40/56/84068311_p0_square1200.jpg",
                    "description":"",
                    "tags":[
                        "KDA",
                        "K/DA",
                        "Ahri(K/DA)",
                        "Ahri",
                        "League_of_Legends",
                        "英雄联盟",
                        "おっぱい",
                        "巨乳",
                        "腋",
                        "腹筋"
                    ],
                    "userId":"15589982",
                    "userName":"Zumi",
                    "width":720,
                    "height":1080,
                    "pageCount":1,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#KDA K/DA Ahri - Zumi的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2020-08-31T21:40:56+09:00",
                    "updateDate":"2020-08-31T21:40:56+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2018/11/19/11/07/20/15032175_aa3a7f609ba524f704f867865265a549_50.jpg"
                },
                {
                    "id":"71574800",
                    "title":"K/DA PopStar Ahri",
                    "illustType":0,
                    "xRestrict":0,
                    "restrict":0,
                    "sl":2,
                    "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2018/11/09/19/49/37/71574800_p0_square1200.jpg",
                    "description":"",
                    "tags":[
                        "Lol",
                        "ahri",
                        "아리",
                        "k/da",
                        "League_of_Legends",
                        "Ahri",
                        "K/DA",
                        "Ahri(K/DA)",
                        "KDA",
                        "おっぱい"
                    ],
                    "userId":"12981691",
                    "userName":"sylee",
                    "width":2159,
                    "height":3000,
                    "pageCount":1,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#Lol K/DA PopStar Ahri - sylee的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2018-11-09T19:49:37+09:00",
                    "updateDate":"2018-11-09T19:49:37+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2019/07/04/02/32/59/15965158_cc5f040e839ef80fc7952eb658775eae_50.png"
                },
                {
                    "id":"84015440",
                    "title":"Seraphine Shower Time",
                    "illustType":0,
                    "xRestrict":0,
                    "restrict":0,
                    "sl":2,
                    "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/08/29/21/44/45/84015440_p0_square1200.jpg",
                    "description":"",
                    "tags":[
                        "Seraphine",
                        "KDA",
                        "英雄联盟",
                        "LOL",
                        "League_of_Legends",
                        "세라핀",
                        "極上の女体",
                        "巨乳",
                        "シャワー",
                        "おっぱい"
                    ],
                    "userId":"57824462",
                    "userName":"FoxyRain",
                    "width":1000,
                    "height":1400,
                    "pageCount":3,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#Seraphine Seraphine Shower Time - FoxyRain的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2020-08-29T21:44:45+09:00",
                    "updateDate":"2020-08-29T21:44:45+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2020/11/27/21/11/43/19736260_aba7fe9f0c4c740f834678e3ad953b99_50.png"
                },
                {
                    "id":"71592821",
                    "title":"KDA akali",
                    "illustType":0,
                    "xRestrict":0,
                    "restrict":0,
                    "sl":2,
                    "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2018/11/10/22/16/21/71592821_p0_square1200.jpg",
                    "description":"",
                    "tags":[
                        "leagueoflegends",
                        "akali",
                        "KDA",
                        "K/DA",
                        "Akali(K/DA)"
                    ],
                    "userId":"17439308",
                    "userName":"pan4",
                    "width":1859,
                    "height":1000,
                    "pageCount":1,
                    "isBookmarkable":true,
                    "bookmarkData":null,
                    "alt":"#leagueoflegends KDA akali - pan4的插画",
                    "isAdContainer":false,
                    "titleCaptionTranslation":{
                        "workTitle":"",
                        "workCaption":""
                    },
                    "createDate":"2018-11-10T22:16:21+09:00",
                    "updateDate":"2018-11-10T22:16:21+09:00",
                    "isUnlisted":false,
                    "profileImageUrl":"https://i.pximg.net/user-profile/img/2020/04/26/14/34/37/18416681_f55852668b9d441353c0ca9119471553_50.jpg"
                }
            ]
        },
        "relatedTags":[
            "League_of_Legends",
            "英雄联盟",
            "LOL",
            "Evelynn",
            "Ahri",
            "K/DA",
            "akali",
            "fanart",
            "ahri",
            "おっぱい",
            "leagueoflegends",
            "Seraphine(KDA)",
            "Kaisa",
            "Evelynn(K/DA)",
            "尻神様",
            "Leagueoflegends"
        ],
        "tagTranslation":{
            "英雄联盟":{
                "zh":"League of Legends"
            },
            "おっぱい":{
                "zh":"欧派"
            },
            "尻神様":{
                "zh":"尻神样"
            }
        },
        "zoneConfig":{
            "header":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=header&format=js&s=2&up=1&a=40&ng=g&l=zh&uri=%2Fajax%2Fsearch%2Fartworks%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pgl8kwaszgnhru3wi&num=5fc6288d759&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "footer":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=footer&format=js&s=2&up=1&a=40&ng=g&l=zh&uri=%2Fajax%2Fsearch%2Fartworks%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pgl8kwaszkjgh9844&num=5fc6288d152&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "infeed":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=illust_search_grid&format=js&s=2&up=1&a=40&ng=g&l=zh&uri=%2Fajax%2Fsearch%2Fartworks%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pgl8kwasznaozx7no&num=5fc6288d190&t=IVwLyT8B6k&t=RcahSSzeRf"
            }
        },
        "extraData":{
            "meta":{
                "title":"#KDAのイラスト・マンガ作品(投稿超过1000件） - pixiv",
                "description":"pixiv",
                "canonical":"https://www.pixiv.net/tags/KDA",
                "alternateLanguages":{
                    "ja":"https://www.pixiv.net/tags/KDA",
                    "en":"https://www.pixiv.net/en/tags/KDA"
                },
                "descriptionHeader":"pixiv"
            }
        }
    }
}
```

+ **国内访问**：

要想在国内访问图片，需要解析返回json的

```text
response["body"]["illustManga"]["data"][index]["url"]
```
   - 这里借用其他人的域名，感谢http://pixiviz.pwp.app/提供的服务，**仅需将国外域名换成国内域名即可**
   - pixiv真实url：https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/11/29/22/36/14/85992188_p0_square1200.jpg
   - 替换后的url： https://i.pixiv.cat/c/250x250_80_a2/img-master/img/2020/11/29/22/36/14/85992188_p0_square1200.jpg

### 2. 排行榜

+ method：get

+ api： https://www.pixiv.net/ranking.php

+ params：

```python
params = {
    "content": "",
    "mode":"",
    "p":"",
    "date": "20201129",
    "format": "json",
    
}
```

> content

|content|描述|
|:-----:|:----:|
|all|	所有|
|illust|	插画|
|manga|	漫画|
|ugoira|	动图|

> mode

|mode|描述|
|:-----:|:----:|
|daily|	每日|
|weekly|	每周|
|monthly|	每月|
|rookie|	新画师|
|original|	原创|
|male|	男性向|
|female|	女性向|
|daily_r18|	每日工口|
|weekly_r18|	每周工口|
|male_r18|	男性工口|
|female_r18|	女性腐向|
|r18g|	工口加强型（猎奇）|

> date: yyyymmdd格式

> p: 起始页（默认为1）

### 3. 获取目标画师的作品集

1. 先获取画师的所有作品的id

https://www.pixiv.net/ajax/user/2283717/profile/all

作品集： `response["body"]["illusts"]` 为字典，键名就是作品的id

2. 根据目标id获取缩略图作品

- url: https://www.pixiv.net/ajax/user/画师id/profile/illusts

- params:

```text
https://www.pixiv.net/ajax/user/2283717/profile/illusts?ids[]=81748865&ids[]=81683752&ids[]=81591637
&ids[]=81489456&ids[]=81438456&ids[]=81365370&ids[]=81243639&ids[]=81243349&ids[]=81050988&ids[]=80982762
&ids[]=80892421&ids[]=80787305&ids[]=80715638&ids[]=80651365&ids[]=80598017&ids[]=80518715&ids[]=80463498
...
&work_category=illustManga&is_first_page=0&lang=zh
```

|params| 必要性 |描述 |
|:----:|:----:|:----:|
|ids[] | Y | 作品id集|
|work_category | Y | 作品类型|
|is_first_page | Y | 是否为第一页|
|lang | N | 语言类型|

ps：is_first_page的值仅有0或1(1表示为第一页，但0或1的返回值的却是一样的，应该是前端判断0或1然后选择加载样式)

- 返回结果：

```json
{
    "error":false,
    "message":"",
    "body":{
        "works":{
            "82295691":{
                "id":"82295691",
                "title":"Atago",
                "illustType":0,
                "xRestrict":0,
                "restrict":0,
                "sl":4,
                "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/06/14/00/17/06/82295691_p0_square1200.jpg",
                "description":"",
                "tags":[
                    "碧蓝航线",
                    "アズールレーン",
                    "atago",
                    "愛宕(アズールレーン)",
                    "真夏の行進曲",
                    "胸膝位",
                    "アズールレーン5000users入り"
                ],
                "userId":"2283717",
                "userName":"風の行者",
                "width":1500,
                "height":844,
                "pageCount":1,
                "isBookmarkable":true,
                "bookmarkData":null,
                "alt":"#碧蓝航线 Atago - 風の行者的插画",
                "isAdContainer":false,
                "titleCaptionTranslation":{
                    "workTitle":"",
                    "workCaption":""
                },
                "createDate":"2020-06-13T20:52:37+09:00",
                "updateDate":"2020-06-14T00:17:06+09:00",
                "isUnlisted":false,
                "profileImageUrl":"https://i.pximg.net/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_50.jpg"
            },
            "82423369":{
                "id":"82423369",
                "title":"Rhea",
                "illustType":0,
                "xRestrict":0,
                "restrict":0,
                "sl":6,
                "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/06/19/17/34/13/82423369_p0_square1200.jpg",
                "description":"",
                "tags":[
                    "Rhea",
                    "LastOrigin",
                    "라스트오리진",
                    "오베로니아레아",
                    "仰臥"
                ],
                "userId":"2283717",
                "userName":"風の行者",
                "width":844,
                "height":1500,
                "pageCount":1,
                "isBookmarkable":true,
                "bookmarkData":null,
                "alt":"#Rhea Rhea - 風の行者的插画",
                "isAdContainer":false,
                "titleCaptionTranslation":{
                    "workTitle":"",
                    "workCaption":""
                },
                "createDate":"2020-06-19T17:34:13+09:00",
                "updateDate":"2020-06-19T17:34:13+09:00",
                "isUnlisted":false,
                "profileImageUrl":"https://i.pximg.net/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_50.jpg"
            },
            "85868165":{
                "id":"85868165",
                "title":"Chizuru Mizuhara",
                "illustType":0,
                "xRestrict":0,
                "restrict":0,
                "sl":4,
                "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/11/24/00/03/38/85868165_p0_square1200.jpg",
                "description":"",
                "tags":[
                    "水原千鶴",
                    "彼女、お借りします"
                ],
                "userId":"2283717",
                "userName":"風の行者",
                "width":844,
                "height":1500,
                "pageCount":1,
                "isBookmarkable":true,
                "bookmarkData":null,
                "alt":"#水原千鶴 Chizuru Mizuhara - 風の行者的插画",
                "isAdContainer":false,
                "titleCaptionTranslation":{
                    "workTitle":"",
                    "workCaption":""
                },
                "createDate":"2020-11-24T00:03:38+09:00",
                "updateDate":"2020-11-24T00:03:38+09:00",
                "isUnlisted":false,
                "profileImageUrl":"https://i.pximg.net/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_50.jpg"
            },
            "85941851":{
                "id":"85941851",
                "title":"Ps 5 princess！",
                "illustType":0,
                "xRestrict":0,
                "restrict":0,
                "sl":4,
                "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/11/27/22/17/13/85941851_p0_square1200.jpg",
                "description":"",
                "tags":[
                    "PS5",
                    "巨乳"
                ],
                "userId":"2283717",
                "userName":"風の行者",
                "width":844,
                "height":1500,
                "pageCount":1,
                "isBookmarkable":true,
                "bookmarkData":null,
                "alt":"#PS5 Ps 5 princess！ - 風の行者的插画",
                "isAdContainer":false,
                "titleCaptionTranslation":{
                    "workTitle":"",
                    "workCaption":""
                },
                "createDate":"2020-11-27T22:17:13+09:00",
                "updateDate":"2020-11-27T22:17:13+09:00",
                "isUnlisted":false,
                "profileImageUrl":"https://i.pximg.net/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_50.jpg"
            },
            "86050649":{
                "id":"86050649",
                "title":"Soaring sword fiora！",
                "illustType":0,
                "xRestrict":0,
                "restrict":0,
                "sl":4,
                "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/12/02/20/23/26/86050649_p0_square1200.jpg",
                "description":"",
                "tags":[
                    "League_of_Legends",
                    "英雄联盟",
                    "fiora"
                ],
                "userId":"2283717",
                "userName":"風の行者",
                "width":844,
                "height":1500,
                "pageCount":1,
                "isBookmarkable":true,
                "bookmarkData":null,
                "alt":"#League_of_Legends Soaring sword fiora！ - 風の行者的插画",
                "isAdContainer":false,
                "titleCaptionTranslation":{
                    "workTitle":"",
                    "workCaption":""
                },
                "createDate":"2020-12-02T20:23:26+09:00",
                "updateDate":"2020-12-02T20:23:26+09:00",
                "isUnlisted":false,
                "profileImageUrl":"https://i.pximg.net/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_50.jpg"
            }
        },
        "zoneConfig":{
            "header":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=header&format=js&s=2&up=1&a=40&ng=w&l=zh&uri=%2Fajax%2Fuser%2F_PARAM_%2Fprofile%2Fillusts&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglavmkcba5t1t77i&num=5fc8c76b371&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "footer":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=footer&format=js&s=2&up=1&a=40&ng=w&l=zh&uri=%2Fajax%2Fuser%2F_PARAM_%2Fprofile%2Fillusts&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglavmkcbg9wpjko7&num=5fc8c76b785&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "logo":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=logo_side&format=js&s=2&up=1&a=40&ng=w&l=zh&uri=%2Fajax%2Fuser%2F_PARAM_%2Fprofile%2Fillusts&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglavmkcbvfm7w26p&num=5fc8c76b264&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "500x500":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=bigbanner&format=js&s=2&up=1&a=40&ng=w&l=zh&uri=%2Fajax%2Fuser%2F_PARAM_%2Fprofile%2Fillusts&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglavmkcby4nhdt17&num=5fc8c76b614&t=IVwLyT8B6k&t=RcahSSzeRf"
            }
        },
        "extraData":{
            "meta":{
                "title":"風の行者的插图・漫画 - pixiv",
                "description":"pixiv",
                "canonical":"https://www.pixiv.net/users/2283717/artworks",
                "ogp":{
                    "description":"微博：   https://weibo.com/turewindwalker twitter：https://twitter.com/TUREwindwalker",
                    "image":"https://i.pximg.net/c/200x200/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_170.jpg",
                    "title":"風の行者的插图・漫画 - pixiv",
                    "type":"article"
                },
                "twitter":{
                    "description":"微博：   https://weibo.com/turewindwalker twitter：https://twitter.com/TUREwindwalker",
                    "image":"https://i.pximg.net/c/200x200/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_170.jpg",
                    "title":"風の行者的插图・漫画 - pixiv",
                    "card":"summary"
                },
                "alternateLanguages":{
                    "ja":"https://www.pixiv.net/users/2283717/artworks",
                    "en":"https://www.pixiv.net/users/2283717/artworks"
                },
                "descriptionHeader":"注册pixiv，就可以对風の行者的作品点“赞！”，还能给他（她）发送信息进行交流。"
            }
        }
    }
}
```

3. 单张作品的详细内容

+ api： https://www.pixiv.net/ajax/illust/作品id (e.g., https://www.pixiv.net/ajax/illust/78703406 )

+ 返回值：

```json
{
    "error":false,
    "message":"",
    "body":{
        "illustId":"78703406",
        "illustTitle":"龍鳳！",
        "createDate":"2020-01-04T05:10:48+00:00",
        "uploadDate":"2020-01-04T05:10:48+00:00",
        "restrict":0,
        "xRestrict":1,
        "sl":6,
        "urls":{
            "mini":"https://i.pximg.net/c/48x48/img-master/img/2020/01/04/14/10/48/78703406_p0_square1200.jpg",
            "thumb":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/01/04/14/10/48/78703406_p0_square1200.jpg",
            "small":"https://i.pximg.net/c/540x540_70/img-master/img/2020/01/04/14/10/48/78703406_p0_master1200.jpg",
            "regular":"https://i.pximg.net/img-master/img/2020/01/04/14/10/48/78703406_p0_master1200.jpg",
            "original":"https://i.pximg.net/img-original/img/2020/01/04/14/10/48/78703406_p0.jpg"
        },
        "tags":{
            "authorId":"2283717",
            "isLocked":false,
            "tags":[
                {
                    "tag":"R-18",
                    "locked":true,
                    "deletable":false,
                    "userId":"2283717",
                    "userName":"風の行者"
                },
                {
                    "tag":"アズールレーン",
                    "locked":true,
                    "deletable":false,
                    "userId":"2283717",
                    "translation":{
                        "en":"碧蓝航线"
                    },
                    "userName":"風の行者"
                },
                {
                    "tag":"龍鳳",
                    "locked":true,
                    "deletable":false,
                    "userId":"2283717",
                    "translation":{
                        "en":"Ryuho"
                    },
                    "userName":"風の行者"
                },
                {
                    "tag":"龍鳳(アズールレーン)",
                    "locked":false,
                    "deletable":true,
                    "translation":{
                        "en":"龙凤（碧蓝航线）"
                    }
                },
                {
                    "tag":"鳳舞う正月",
                    "locked":false,
                    "deletable":true
                },
                {
                    "tag":"オナニー",
                    "locked":false,
                    "deletable":true,
                    "translation":{
                        "en":"自慰"
                    }
                },
                {
                    "tag":"アズールレーン1000users入り",
                    "locked":false,
                    "deletable":true,
                    "translation":{
                        "en":"碧蓝航线1000users加入书籤"
                    }
                }
            ],
            "writable":true
        },
        "alt":"#アズールレーン 龍鳳！ - 風の行者的插画",
        "storableTags":[
            "0xsDLqCEW6",
            "RcahSSzeRf",
            "_BX8YvENe3",
            "lzti5TKD1I",
            "JW9dL6YfaY",
            "xjfPXTyrpQ",
            "FqVQndhufZ"
        ],
        "userId":"2283717",
        "userName":"風の行者",
        "userAccount":"hjl00100",
        "userIllusts":{
            "25567076":null,
            "25567225":null,
            "25567393":null,
            "78574008":null,
            "78648399":{
                "id":"78648399",
                "title":"happy new year！",
                "illustType":0,
                "xRestrict":0,
                "restrict":0,
                "sl":4,
                "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/01/01/21/41/46/78648399_p0_square1200.jpg",
                "description":"",
                "tags":[
                    "アズールレーン",
                    "龍鳳",
                    "龍鳳(アズールレーン)",
                    "謹賀新年",
                    "鳳舞う正月",
                    "アズールレーン1000users入り"
                ],
                "userId":"2283717",
                "userName":"風の行者",
                "width":1778,
                "height":1000,
                "pageCount":1,
                "isBookmarkable":true,
                "bookmarkData":null,
                "alt":"#アズールレーン happy new year！ - 風の行者的插画",
                "isAdContainer":false,
                "titleCaptionTranslation":{
                    "workTitle":"",
                    "workCaption":""
                },
                "createDate":"2020-01-01T21:41:46+09:00",
                "updateDate":"2020-01-01T21:41:46+09:00",
                "isUnlisted":false,
                "profileImageUrl":"https://i.pximg.net/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_50.jpg"
            },
            "78703406":{
                "id":"78703406",
                "title":"龍鳳！",
                "illustType":0,
                "xRestrict":1,
                "restrict":0,
                "sl":6,
                "url":"https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/01/04/14/10/48/78703406_p0_square1200.jpg",
                "tags":[
                    "R-18",
                    "アズールレーン",
                    "龍鳳",
                    "龍鳳(アズールレーン)",
                    "鳳舞う正月",
                    "オナニー",
                    "アズールレーン1000users入り"
                ],
                "userId":"2283717",
                "userName":"風の行者",
                "width":1778,
                "height":1000,
                "pageCount":4,
                "isBookmarkable":true,
                "bookmarkData":null,
                "alt":"#アズールレーン 龍鳳！ - 風の行者的插画",
                "isAdContainer":false,
                "titleCaptionTranslation":{
                    "workTitle":"",
                    "workCaption":""
                },
                "createDate":"2020-01-04T14:10:48+09:00",
                "updateDate":"2020-01-04T14:10:48+09:00",
                "isUnlisted":false
            }
        },
        "likeData":false,
        "width":1778,
        "height":1000,
        "pageCount":4,
        "bookmarkCount":3765,
        "likeCount":2360,
        "commentCount":7,
        "responseCount":0,
        "viewCount":51916,
        "isHowto":false,
        "isOriginal":false,
        "imageResponseOutData":[

        ],
        "imageResponseData":[

        ],
        "imageResponseCount":0,
        "pollData":null,
        "seriesNavData":null,
        "descriptionBoothId":null,
        "descriptionYoutubeId":null,
        "comicPromotion":null,
        "fanboxPromotion":{
            "userName":"風の行者",
            "userImageUrl":"https://i.pximg.net/user-profile/img/2018/04/22/11/05/57/14125733_ab43f73788b0aee91990e89cfda26af1_170.jpg",
            "contentUrl":"https://www.pixiv.net/fanbox/creator/2283717?utm_campaign=www_artwork&utm_medium=site_flow&utm_source=pixiv",
            "description":"微博：   https://weibo.com/turewindwalker twitter：https://twitter.com/TUREwindwalker",
            "imageUrl":"https://pixiv.pximg.net/c/520x280_90_a2_g5/fanbox/public/images/creator/2283717/cover/seD9i94kGrwnXdjiALwwJoxx.jpeg",
            "imageUrlMobile":"https://pixiv.pximg.net/c/520x280_90_a2_g5/fanbox/public/images/creator/2283717/cover/seD9i94kGrwnXdjiALwwJoxx.jpeg",
            "hasAdultContent":true
        },
        "contestBanners":[

        ],
        "isBookmarkable":true,
        "bookmarkData":null,
        "contestData":null,
        "zoneConfig":{
            "responsive":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=illust_responsive&format=js&s=2&up=1&a=40&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglaw765i4i39alj3&num=5fc8cc0f619&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "rectangle":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=illust_rectangle&format=js&s=2&up=1&a=40&ng=r&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglaw765i8opj87dd&num=5fc8cc0f262&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "500x500":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=bigbanner&format=js&s=2&up=1&a=40&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglaw765ibv2j6axa&num=5fc8cc0f635&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "header":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=header&format=js&s=2&up=1&a=40&ng=r&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglaw765ifbi7t4x8&num=5fc8cc0f348&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "footer":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=footer&format=js&s=2&up=1&a=40&ng=r&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglaw765iipml0k44&num=5fc8cc0f909&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "expandedFooter":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=multiple_illust_viewer&format=js&s=2&up=1&a=40&ng=g&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglaw765iloy78xnu&num=5fc8cc0f569&t=IVwLyT8B6k&t=RcahSSzeRf"
            },
            "logo":{
                "url":"https://pixon.ads-pixiv.net/show?zone_id=logo_side&format=js&s=2&up=1&a=40&ng=r&l=zh&uri=%2Fajax%2Fillust%2F_PARAM_&is_spa=1&K=7a1013a035198&ab_test_digits_first=9&yuid=JTBElwA&suid=Pglaw765ip67zexg0&num=5fc8cc0f888&t=IVwLyT8B6k&t=RcahSSzeRf"
            }
        },
        "extraData":{
            "meta":{
                "title":"#アズールレーン 龍鳳！ - 風の行者的插画 - pixiv",
                "description":"この作品 「龍鳳！」 は 「R-18」「アズールレーン」 等のタグがつけられた「風の行者」さんのイラストです。 「Drawing process video will be added to the reward this month! Thank you for your s…",
                "canonical":"https://www.pixiv.net/artworks/78703406",
                "alternateLanguages":{
                    "ja":"https://www.pixiv.net/artworks/78703406",
                    "en":"https://www.pixiv.net/en/artworks/78703406"
                },
                "descriptionHeader":"本作「龍鳳！」为附有「R-18」「アズールレーン」等标签的插画。",
                "ogp":{
                    "description":"Drawing process video will be added to the reward this month! Thank you for your support！you can sup",
                    "image":"https://s.pximg.net/www/images/pixiv_logo.gif?2",
                    "title":"#アズールレーン 龍鳳！ - 風の行者的插画 - pixiv",
                    "type":"article"
                }
            }
        },
        "titleCaptionTranslation":{
            "workTitle":"",
            "workCaption":""
        },
        "isUnlisted":false,
        "request":null
    }
}
```

+ 单作品id可能存在多张图片，怎么确认？

注意每一张图片的url都有 `作品id_pX` ，**pX的X就是代表第几张图片，X的取值来自返回json的pageCount**

https://i.pximg.net/img-master/img/2020/01/11/02/20/17/78829558_p0_master1200.jpg
https://i.pximg.net/img-master/img/2020/01/11/02/20/17/78829558_p1_master1200.jpg
https://i.pximg.net/img-master/img/2020/01/11/02/20/17/78829558_p2_master1200.jpg
https://i.pximg.net/img-master/img/2020/01/11/02/20/17/78829558_p3_master1200.jpg