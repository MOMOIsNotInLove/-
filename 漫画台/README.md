# 漫画台加密原理

- 目标网址： **https://m.manhuatai.com/**

- 几个API：
   + PC端漫画大全： https://www.manhuatai.com/api/getComicList/?product_id=2&productname=mht&platformname=**PC**
   + 移动端漫画大全： https://www.manhuatai.com/api/getComicList/?product_id=2&productname=mht&platformname=**wap**
   + 某部漫画详情：https://www.manhuatai.com/漫画名中文拼音全称/ （漫画名大全由上述两个api获取）
   
- 加密js文件

   通过一系列的尝试，知道了漫画台的加密原理：***核心JavaScript加密文件就在网页源代码里，可以直接正则表达式提取***，如下

```javascript
window.$definitions={low:"-mht.low",middle:"-mht.middle",high:"-mht.high"};
window.pageType="read";
window.comicInfo={
    comic_id:27417,comic_newid:"yaoshenji",comic_name:"妖神记",last_chapter_id:"1724950",
    last_chapter_newid:"di276hua2-1590226030015",last_chapter_name:"第276话2 黑炎淬炼",
    show_type:1,readtype:0,comic_status:1,charge_paid:0,charge_coin_free:1,update_time:159022603e4,
    boo_virtual_coin:!0,charge_status:"10000000000000000000",charge_share_free:1,charge_advertise_free:1,
    charge_truetime_free:1,charge_limittime_free:1,charge_limitline_free:1,charge_vip_free:1,charge_spread_free:1,
    charge_game_free:1,charge_coupons_free:1,charge_lottery_free:1,charge_limittime_paid:1,charge_limitline_paid:1,
    charge_others_paid:1,charge_credit_paid:1,is_copyright:1,current_chapter:{chapter_name:"第133话2 不错的年轻人",
    chapter_newid:"194",chapter_id:1379477,chapter_domain:"dm300.com",start_num:1,end_num:8,price:0,
    chapter_image_addr:"/feature/1379477_2_1.jpg",create_date:1548466403710,rule:"/comic/Y/妖神记/第133话2F1/$$.jpg"},
    prev_chapter:{chapter_id:1377156,chapter_newid:"193",chapter_name:"第133话1 不错的年轻人",price:0,
    chapter_image_addr:"/feature/1377156_2_1.jpg",create_time:"2019-01-26T01:33:23.733Z",topic_copyright:"",
    chapter_domain:"dm300.com",rule:"/comic/Y/妖神记/第133话1F1/$$.jpg",start_num:1,end_num:9,create_date:1548466403710},
    next_chapter:{chapter_id:1381191,chapter_newid:"195",chapter_name:"第134话1 支援到达",price:0,
    chapter_image_addr:"/feature/1381191_2_1.jpg",create_time:"2019-01-26T01:33:23.697Z",topic_copyright:"",
    chapter_domain:"jumanhua.com",rule:"/comic/Y/妖神记/134-1话/$$.jpg",start_num:1,end_num:9,create_date:1548466403710},
    seoTitleTemplate:{default:"{0}{1} {0}漫画{1}",title:"{0}{1}话 {2} {0}漫画{1}话 {2} {0}{1}回 {2} 漫画台"}
}
```

经过发现，加密的原理与知音漫客相差无几，甚至更简单，因为图片的地址直接在script文件中已经显示了，主要注意三个点：
+ rule:"/comic/Y/妖神记/第133话2F1/$$.jpg" ~图片的src为：**/comic/Y/妖神记/第133话2F1/**
+ start_num:1~图片的开始页数
+ end_num:8~图片的截止页数

完整的图片url：https://mhpic.dm300.com/**rule**/**页数**.jpg-mht.middle.webp
eg：https://mhpic.dm300.com/comic/J/绝世唐门/第541话F0_258794/11.jpg-mht.middle.webp


