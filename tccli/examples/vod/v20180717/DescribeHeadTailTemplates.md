**Example 1: 获取片头片尾模板列表**

获取片头片尾模板列表

Input: 

```
tccli vod DescribeHeadTailTemplates --cli-unfold-argument  \
    --Definitions 10000
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "12ae8d8e-dce3-4151-9d4b-5594145287e1",
        "HeadTailTemplateSet": [
            {
                "Definition": 10000,
                "HeadCandidateSet": [
                    "123xxx000"
                ],
                "FillType": "black",
                "Name": "模板号",
                "Comment": "模板描述",
                "TailCandidateSet": [
                    "1230xxx99"
                ]
            }
        ]
    }
}
```

