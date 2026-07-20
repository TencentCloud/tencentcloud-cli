**Example 1: 查看企业下的员工列表**



Input: 

```
tccli adp DescribeAccountList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10 \
    --FilterList.0.Name SpaceId \
    --FilterList.0.ValueList default_space
```

Output: 
```
{
    "Response": {
        "AccountList": [
            {
                "AccountUin": "700002740513",
                "Avatar": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/public/avatar_rabbit02.png",
                "NickName": "lzh"
            }
        ],
        "TotalCount": "99",
        "RequestId": "1df743c6-37d2-4890-b305-933ed27923c6"
    }
}
```

