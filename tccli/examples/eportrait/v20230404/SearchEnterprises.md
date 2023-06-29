**Example 1: SearchEnterprises1**

SearchEnterprises1

Input: 

```
tccli eportrait SearchEnterprises --cli-unfold-argument  \
    --Name 腾讯科技 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Eid": "4e8eb65c5f996b50e9b8e93be211a483",
                "Name": "腾讯科技（成都）有限公司",
                "SearchName": "腾讯科技（成都）有限公司",
                "SearchNameType": "abbr"
            },
            {
                "Eid": "57b5f768b3d0c612db748516e0e2f335",
                "Name": "北京嘉和腾讯科技有限公司",
                "SearchName": "北京嘉和腾讯科技有限公司",
                "SearchNameType": "abbr"
            },
            {
                "Eid": "5aa4eefcc80fa62a9db98bc96ba35981",
                "Name": "山西龙腾讯科技有限公司",
                "SearchName": "山西龙腾讯科技有限公司",
                "SearchNameType": "abbr"
            },
            {
                "Eid": "5eef1151c5c8c328c9b31fcf9cbacfc3",
                "Name": "腾讯科技（深圳）有限公司",
                "SearchName": "腾讯科技（深圳）有限公司",
                "SearchNameType": "abbr"
            },
            {
                "Eid": "b40e8cea06a0019d4b12d3913b269fc9",
                "Name": "北京四海腾讯科技有限责任公司",
                "SearchName": "北京四海腾讯科技有限责任公司",
                "SearchNameType": "abbr"
            },
            {
                "Eid": "d19588af77665b32b1db3977e2428123",
                "Name": "腾讯科技（武汉）有限公司",
                "SearchName": "腾讯科技（武汉）有限公司",
                "SearchNameType": "abbr"
            },
            {
                "Eid": "e3e41dce9bbd62a5db5a8c9667969103",
                "Name": "广州腾讯科技有限公司",
                "SearchName": "广州腾讯科技有限公司",
                "SearchNameType": "abbr"
            }
        ],
        "OffSet": 10,
        "RequestId": "3ee21f34-e917-4cd2-b692-0b4523a360f3",
        "TotalCount": 7
    }
}
```

