## pixiv

- [x] 解析api接口
   - [x] 搜索
   - [x] 排行榜


**使用前提：** 能够访问国外网络

### 1. 搜索

+ method：get

+ api：

https://www.pixiv.net/ajax/search/artworks/<搜索关键词>?order=<>&mode=<>&p=<>&s_mode=<>&type=<>&lang=<>

+ params：


| 字段 | 类型 | 必要性 | 描述 | 备注 |
|:----:|:----:|:----:|:----:|:----:|
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

+ 国内访问：

要想在国内访问图片，需要解析返回json的

```text
response["body"]["illustManga"]["data"][index]["url"]
```
   - 这里借用其他人的域名，将相关数据进行替换，换成国内域名
   - pixiv真实url：https://i.pximg.net/c/250x250_80_a2/img-master/img/2020/11/29/22/36/14/85992188_p0_square1200.jpg
   - 替换后的url：https://i.pixiv.cat/img-original/img-master/img/2020/11/29/22/36/14/85992188_p0.jpg

### 2.排行榜

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

|content|	描述|
|:-----:|:----:|
|all|	所有|
|illust|	插画|
|manga|	漫画|
|ugoira|	动图|

> mode

|daily|	每日|
|:----:|:----:|
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
> p: 起始页（1）