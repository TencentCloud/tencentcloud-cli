**Example 1: 实体信息查询**

给定实体的名称或id，查询实体的所有属性和属性值。常用于个性化推荐、搜索，智能问答等业务场景。

Input: 

```
tccli tkgdq DescribeEntity --cli-unfold-argument  \
    --EntityName 腾讯云
```

Output: 
```
{
  "Response": {
    "Content": "{"Foundin":[{"Name":"http://baike.baidu.com/item/%E8%85%BE%E8%AE%AF%E4%BA%91"},{"Name":"http://baike.baidu.com/item/%E8%85%BE%E8%AE%AF%E4%BA%91/9905046"},{"Name":"http://baike.baidu.com/view/10880522.htm"}],"Id":[{"Name":"205565918609303992"}],"ImageDigest":[{"Name":"1fbf6a63b562ce566635b09342ecd91a","Order":1000}],"Name":[{"Name":"腾讯云"}],"Popular":[{"Name":523}],"RichName":[{"Name":"腾讯云"}],"Type":[{"Name":"科技产品类_产品 (174)"}],"Types":[{"Name":174}],"Uuid":[{"Name":"87bc7630-9ed9-4bf0-a3d6-363eeeac4e21"}],"中文名":[{"Name":"腾讯云","Order":0}],"使用领域":[{"Name":"社交","Order":0},{"Name":"游戏和其他领域","Order":1}],"原始名称":[{"Name":"腾讯云","Order":1}],"名称":[{"Name":"腾讯云","Order":0}],"外文名":[{"Name":"qcloud","Order":0}],"应用":[{"Name":"云空间","Order":0}],"相关实体":[{"Name":"云服务器","Order":1},{"Id":"6983952906450524110","Name":"行业解决方案","Order":1,"Popular":380},{"Name":"阿里云","Order":1},{"Id":"325666091772717664","Name":"阿里云","Order":1,"Popular":615},{"Name":"云服务","Order":1},{"Id":"9062208975046697975","Name":"云服务器","Order":1,"Popular":548},{"Name":"行业解决方案","Order":1},{"Id":"1146499194548693386","Name":"云服务","Order":1,"Popular":593}],"简介":[{"Name":"腾讯云有着深厚的基础架构,并且有着多年对海量互联网服务的经验,不管是社交、游戏还是其他领域,都有多年的成熟产品来提供产品服务。腾讯在云端完成重要部署,为开发者及企业提供云服务、云数据、云运营等整体一站式服务方案。|@|具体包括云服务器、云存储、云数据库和弹性web引擎等基础云服务；腾讯云分析(mta)、腾讯云推送(信鸽)等腾讯整体大数据能力；以及 qq互联、qq空间、微云、微社区等云端链接社交体系。这些正是腾讯云可以提供给这个行业的差异化优势,造就了可支持各种互联网使用场景的高品质的腾讯云技术平台。","Order":0}],"类别":[{"Name":"互联网","Order":0}],"精选上位词":[{"Name":"产品","Order":1},{"Name":"成熟产品来提供产品服务","Order":1},{"Name":"互联网","Order":1}],"精选别名":[{"Name":"腾讯云"}],"英文名":[{"Name":"qcloud","Order":0}]}",
    "RequestId": "fe0b016c-adc3-48ca-a855-3c3e3e81f664"
  }
}
```

