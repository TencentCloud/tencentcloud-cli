**Example 1: DescribeMNPPreview**



Input: 

```
tccli tcmpp DescribeMNPPreview --cli-unfold-argument  \
    --MNPId mpjl3td541qppx9k \
    --MNPVersionId 2404 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "MNPDesc": "",
            "MNPId": "mpjl3td541qppx9k",
            "MNPName": "autotest_online_miniapp",
            "MNPVersion": "1.0.208",
            "MNPVersionIntro": "test",
            "PreviewEntrancePath": "page/component/index",
            "QRCodeUrl": "http://127.0.0.1/T04257DS9431720WTAG/mpp/mpjl3td541qppx9k-1.0.208-1722585281267.png"
        },
        "RequestId": "775b6c06-19e1-4bf5-bfd7-7eb50c51f488"
    }
}
```

