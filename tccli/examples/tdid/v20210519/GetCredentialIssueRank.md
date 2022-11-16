**Example 1: CredentialIssueRank**

凭证颁发排行

Input: 

```
tccli tdid GetCredentialIssueRank --cli-unfold-argument  \
    --StartTime 2021-06-28 \
    --EndTime 2021-07-28 \
    --ClusterId bcos-fmtkyt8xne
```

Output: 
```
{
    "Response": {
        "RankIssueResult": [
            {
                "Count": 1,
                "ApplyId": 1,
                "ApplyName": "xx",
                "CptName": "xx",
                "Rank": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

