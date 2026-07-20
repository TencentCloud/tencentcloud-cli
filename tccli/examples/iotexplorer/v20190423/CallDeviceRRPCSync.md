**Example 1: 自定义topic模式**



Input: 

```
tccli iotexplorer CallDeviceRRPCSync --cli-unfold-argument  \
    --ProductId N5DBOST040 \
    --DeviceName nandy_dev1 \
    --Payload {"a":"b"} \
    --Topic N5DBOST040/nandy_dev1/evc/param/a
```

Output: 
```
{
    "Response": {
        "ClientToken": "v221.215.133.103MEjCE::79afc8bc-12bf-429b-a48d-e8596c4e918a",
        "MessageId": 54,
        "PayloadBase64": "eyJyc3AiOiJvayJ9",
        "ReplyTopic": "",
        "Status": "Replied",
        "RequestId": "79afc8bc-12bf-429b-a48d-e8596c4e918a"
    }
}
```

**Example 2: 默认topic模式**



Input: 

```
tccli iotexplorer CallDeviceRRPCSync --cli-unfold-argument  \
    --ProductId N5DBOST040 \
    --DeviceName nandy_dev1 \
    --Payload {"a":"b"}
```

Output: 
```
{
    "Response": {
        "ClientToken": "v221.90.233.213aHiQo::1d17f100-cc9e-4458-8199-f22ba6d4ae14",
        "MessageId": 52,
        "PayloadBase64": "eyJyc3AiOiJvayJ9",
        "ReplyTopic": "$iotrrpc/up/N5DBOST040/nandy_dev1/52",
        "Status": "Replied",
        "RequestId": "1d17f100-cc9e-4458-8199-f22ba6d4ae14"
    }
}
```

