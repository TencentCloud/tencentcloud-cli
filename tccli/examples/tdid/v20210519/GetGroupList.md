**Example 1: SetGroupId**

配置主群组

Input: 

```
tccli tdid GetGroupList --cli-unfold-argument  \
    --Status 0 \
    --ClusterId bcos-fmtkyt8xne
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "GroupId": 2,
                "NodeCount": 4,
                "NodeCountOfAgency": 4,
                "Description": "qtadescriptionjkbdcqzgwohei"
            },
            {
                "GroupId": 3,
                "NodeCount": 4,
                "NodeCountOfAgency": 4,
                "Description": "qtadescriptionzmphidguskafr"
            },
            {
                "GroupId": 4,
                "NodeCount": 4,
                "NodeCountOfAgency": 4,
                "Description": "qtadescriptiononjygtkmhlcqp"
            },
            {
                "GroupId": 5,
                "NodeCount": 4,
                "NodeCountOfAgency": 4,
                "Description": "qtadescriptionxhprqfmuvtyod"
            },
            {
                "GroupId": 6,
                "NodeCount": 6,
                "NodeCountOfAgency": 5,
                "Description": "qtaaas"
            },
            {
                "GroupId": 7,
                "NodeCount": 5,
                "NodeCountOfAgency": 5,
                "Description": "1111"
            },
            {
                "GroupId": 8,
                "NodeCount": 5,
                "NodeCountOfAgency": 5,
                "Description": "测试"
            },
            {
                "GroupId": 9,
                "NodeCount": 5,
                "NodeCountOfAgency": 5,
                "Description": "test"
            },
            {
                "GroupId": 10,
                "NodeCount": 5,
                "NodeCountOfAgency": 4,
                "Description": "xxxx"
            }
        ],
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

