**Example 1: SVC新建规则**



Input: 

```
tccli vpc CreateSvcToUsgInternal --cli-unfold-argument  \
    --AddSvcToUsgRequest.0.VpcId 1200 \
    --AddSvcToUsgRequest.0.Protocol 0 \
    --AddSvcToUsgRequest.0.UsgIdList sg-asdqkq \
    --AddSvcToUsgRequest.0.UniqCdcId cdc-aosq293w \
    --AddSvcToUsgRequest.0.SvcId 123123 \
    --AddSvcToUsgRequest.0.VirtualPort 3600 \
    --AddSvcToUsgRequest.0.Vip 12.2.2.3 \
    --AddSvcToUsgRequest.0.Location tgw \
    --AddSvcToUsgRequest.0.AppId 123122 \
    --AddSvcToUsgRequest.0.Type 1
```

Output: 
```
{
    "Response": {
        "AddSvcToUsgResult": [
            {
                "SvcId": "vpce-kifyia9o",
                "ErrorCode": 0,
                "ErrorInfo": "success"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

