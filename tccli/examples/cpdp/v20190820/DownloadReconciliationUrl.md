**Example 1: 对账中心账单下载接口正常返回示例**

对账中心账单下载接口正常返回的示例，用户需要根据返回的地址，进行文件下载。注意文件格式为csv，文件内容的每一列位置不会变化，但会向后进行扩展，注意进行兼容。

Input: 

```
tccli cpdp DownloadReconciliationUrl --cli-unfold-argument  \
    --AppCode cpdp_recon_zhibo35001 \
    --MainAppId 25199477 \
    --BillDate 2021-06-24
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "http://malitong-1249200.cos.ap-guangzhou.myqcloud.com/reconciliation/bus/2511994771624439794510674732_2021-06-24_2.csv?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID7ct6dqAX0QuCNayR3zKAmIZw97TSafMp%26q-sign-time%3D1629788324%3B1629791924%26q-key-time%3D1629788324%3B1629791924%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3D6b420c00de1f44534be4d1431a013bd07a1077da",
        "HashType": "SHA1",
        "HashValue": "055a397d3c7e9fbf97c6348732c20684c89d01df",
        "RequestId": "055a-3c7e-97c-6348-c2068-89d-01df"
    }
}
```

