**Example 1: 查询整颗树**



Input: 

```
tccli billing DescribeAllocationTree --cli-unfold-argument  \
    --Month 2022-11
```

Output: 
```
{
    "Response": {
        "Id": 1,
        "Name": "集团",
        "TreeNodeUniqKey": "909619400-63567fc182c5a",
        "Children": [
            {
                "Id": 2,
                "Name": "财务部",
                "TreeNodeUniqKey": "909619400-63567ffc4a1b3",
                "Children": []
            },
            {
                "Id": 4,
                "Name": "产品部",
                "TreeNodeUniqKey": "909619400-6357486e737c1",
                "Children": [
                    {
                        "Id": 6,
                        "Name": "产品一部",
                        "TreeNodeUniqKey": "909619400-6358ee8995950",
                        "Children": []
                    },
                    {
                        "Id": 7,
                        "Name": "产品二部",
                        "TreeNodeUniqKey": "909619400-6358ee8e7ae35",
                        "Children": []
                    },
                    {
                        "Id": 8,
                        "Name": "产品三部",
                        "TreeNodeUniqKey": "909619400-6358ee9354431",
                        "Children": []
                    },
                    {
                        "Id": 9,
                        "Name": "产品四部",
                        "TreeNodeUniqKey": "909619400-6358ee977ff68",
                        "Children": []
                    },
                    {
                        "Id": 10,
                        "Name": "产品五部",
                        "TreeNodeUniqKey": "909619400-6358ee9c73690",
                        "Children": []
                    }
                ]
            },
            {
                "Id": 5,
                "Name": "组织部",
                "TreeNodeUniqKey": "909619400-6358ee6cb2f8f",
                "Children": []
            }
        ],
        "RequestId": "8e6f00af-4843-481c-9e3a-d61ba53b07ed"
    }
}
```

