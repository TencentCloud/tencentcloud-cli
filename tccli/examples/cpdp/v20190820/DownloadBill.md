**Example 1: 下载对账单请求示例**

本接口提供对账单下载功能。调用者根据本接口返回的URL地址，在D+1日下载对账单。注意，本接口返回的URL地址有时效，请尽快下载。URL超时时效后，请重新调用本接口再次获取。

Input: 

```
tccli cpdp DownloadBill --cli-unfold-argument  \
    --MidasSignature your_midas_signature \
    --StateDate 20191202 \
    --MidasSecretId your_midas_secret_id \
    --MidasAppId test_midas_app_id
```

Output: 
```
{
    "Response": {
        "StateType": "TRADE",
        "FileName": "appid_20191202.csv",
        "FileMD5": "bef046b73c9e543f7773692ce56def68",
        "DownloadUrl": "download_url",
        "RequestId": "0c929116-67b6-4396-9d55-ba4a9113822d"
    }
}
```

