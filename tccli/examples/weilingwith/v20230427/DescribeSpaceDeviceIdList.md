**Example 1: 查询指定空间设备编号列表**

查询指定空间设备编号列表成功响应示例

Input: 

```
tccli weilingwith DescribeSpaceDeviceIdList --cli-unfold-argument  \
    --ElementIds 377a53a6-c5a7-445d-a3b7-c2d721f95408 \
    --IsCascade True \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 10 \
    --ApplicationToken GUsHDOIP614sDxEIiliCx7GIKTqyONoX
```

Output: 
```
{
    "Response": {
        "RequestId": "1c3e7242-f4fb-4000-b8ae-0724b481693d",
        "Result": {
            "DeviceIds": [
                "2b538c57-933f-4820-b1d0-4df70d64aee3",
                "ad655ba1-975a-4238-94d7-5d2015d1cf1f",
                "5a1a0b73-7aa3-4699-a893-21846e7853ec",
                "0a198d6e-40f0-499f-bf99-7a959b7f4ef2"
            ]
        }
    }
}
```

**Example 2: 查询指定空间设备编号列表示例-prod**

查询指定空间设备编号列表示例-prod

Input: 

```
tccli weilingwith DescribeSpaceDeviceIdList --cli-unfold-argument  \
    --ElementIds 306fc545-fc98-4513-ae6e-751f990ae61a \
    --IsCascade True \
    --WorkspaceId 1133 \
    --PageNumber 1 \
    --PageSize 10 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "51ddc6c7-0ee6-4d0d-b95a-dda432859da7",
        "Result": {
            "DeviceIds": [
                "675a9490-dd66-4ac7-b39b-c74977899a1a",
                "14dfa61a-762b-4785-bd39-cd709c6cf3d9",
                "840e3fe7-4eb4-4a64-9036-02ba94956e06",
                "3247728f-15d2-48a2-a0fc-d07a6a6023f0",
                "90f965da-5ed9-469c-bace-7ecd09e2693c",
                "1635422d-5de3-4e38-9f68-94b43fd78185",
                "35bc7027-567a-48d2-a3ee-63c57be9ae9f",
                "749287c4-c48f-42f4-b083-838c1b2fef09",
                "50a294f4-9289-43d0-aa27-efc31c7405ac",
                "3049938c-3048-4fef-a2e8-2843ede35edb"
            ]
        }
    }
}
```

