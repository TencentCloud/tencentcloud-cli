**Example 1: CredentialIssueTrend**

凭证颁发趋势

Input: 

```
tccli tdid GetCredentialIssueTrend --cli-unfold-argument  \
    --ClusterId bcos-fmtkyt8xne \
    --StartTime 2021-07-15 \
    --EndTime 2021-07-28
```

Output: 
```
{
    "Response": {
        "Trend": [
            {
                "Time": "2021-07-15",
                "Count": 0
            },
            {
                "Time": "2021-07-16",
                "Count": 0
            },
            {
                "Time": "2021-07-17",
                "Count": 0
            },
            {
                "Time": "2021-07-18",
                "Count": 0
            },
            {
                "Time": "2021-07-19",
                "Count": 0
            },
            {
                "Time": "2021-07-20",
                "Count": 1
            },
            {
                "Time": "2021-07-21",
                "Count": 0
            },
            {
                "Time": "2021-07-22",
                "Count": 0
            },
            {
                "Time": "2021-07-23",
                "Count": 0
            },
            {
                "Time": "2021-07-24",
                "Count": 0
            },
            {
                "Time": "2021-07-25",
                "Count": 0
            },
            {
                "Time": "2021-07-26",
                "Count": 0
            },
            {
                "Time": "2021-07-27",
                "Count": 0
            }
        ],
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

