**Example 1: 申请单详情**



Input: 

```
tccli bpaas GetApplicationDetail --cli-unfold-argument  \
    --ApplicationId 771
```

Output: 
```
{
    "Response": {
        "BpaasId": "223",
        "CreateTime": "2024-07-08 10:56:47",
        "Name": "申请cdb",
        "Nick": "",
        "Nodes": [
            {
                "ApproveId": "0",
                "ApprovedUin": "0",
                "CreateTime": "2024-07-08 14:23:05",
                "IsApprove": false,
                "Msg": "AssumeRole error",
                "Scf": "helloworld-1618219767",
                "Seq": "1",
                "SubStatus": "3",
                "Title": "节点1",
                "Type": "2",
                "Users": []
            }
        ],
        "Opinions": [
            {
                "Content": [
                    "leader审批"
                ],
                "Seq": "1",
                "Title": "审批字段",
                "Type": "2"
            }
        ],
        "OwnUin": "100000007999",
        "Param": "%7B%22PayPaas%22%3A%5B%7B%22Value%22%3A%7B%22OrderIds.0%22%3A%2220240708289061883544191%22%7D%2C%22Key%22%3A%22queryString%22%7D%5D%7D",
        "Reason": "testing",
        "Status": "2",
        "Uin": "100000007999",
        "RequestId": "5d15e609-d4bb-4237-b5be-f0034738591d"
    }
}
```

