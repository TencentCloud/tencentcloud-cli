**Example 1: 成功**



Input: 

```
tccli iss ListDeviceSnapshots --cli-unfold-argument  \
    --ChannelId c9b87de2-****-41d7****-328****f240 \
    --Start 1740544738 \
    --End 1740573538
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CreatedTime": "2025-02-12 18:05:44",
                "DownloadUrl": "https://******/ipts/snapshot/download?source=NzAwMDAwMzg2NjY5XzI1MTIyODMxM18xOGQ5OGMwNy1iOWIzLTRhZmQtYmNiYi0wY2I2ODEwMDY3OGRfYzliODdkZTItYmUyNi00M*************JmMjQwXzQxYjc3Nzg0LWQ3ZjEtNDBjMS1hMDUyLTE1ZmY1ZTU0MGNmZV8zNDAyMDAwMDAwMTMyMDAwMDAxOTAyMjAyNTAyMTIxODA1NDQwMDAwMi5qcGc=.uqzfPoBi*******A5RtMxjcOt7Hhi_7GVnwSuAW2IWM=&token=cms_**********_e4hu23e90PNAur-OBwEfg",
                "FileName": "3402000000*****************0002.jpg",
                "ImageSize": 545335,
                "PreviewUrl": "https://******/ipts/snapshot/download?source=NzAwMDAwMzg2NjY5XzI1MTIyODMxM18xOGQ5OGMwNy1iOWIzLTRhZmQtYmNiYi0wY2I2ODEwMDY3OGRfYzliODdkZTItYmUyNi00M**************mJmMjQwXzQxYjc3Nzg0LWQ3ZjEtNDBjMS1hMDUyLTE1ZmY1ZTU0MGNmZV8zNDAyMDAwMDAwMTMyMDAwMDAxOTAyMjAyNTAyMTIxODA1NDQwMDAwMi5qcGc=.uqzfPoB********QA5RtMxjcOt7Hhi_7GVnwSuAW2IWM=&token=cms_**********_e4hu23e90PNAur-OBwEfg&preview=true",
                "ReceivedTime": "2025-02-26 16:58:30",
                "SessionId": "16a8h2e8-****-**********-2ed9****82m80"
            }
        ],
        "RequestId": "74a881e8-****-**********-2ed9370480",
        "TotalCount": 1
    }
}
```

