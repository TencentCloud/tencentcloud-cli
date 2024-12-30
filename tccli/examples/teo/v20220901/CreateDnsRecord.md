**Example 1: 创建 DNS 记录**

在 ZoneId 为 zone-225qgrnvbi9w 的站点下，创建一个记录名为 www.example.com，记录类型为 A，记录内容为1.2.3.4，缓存时间为60秒的 DNS 记录。

Input: 

```
tccli teo CreateDnsRecord --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --Name www.example.com \
    --Type A \
    --Content 1.2.3.4 \
    --TTL 60
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "RecordId": "record-225rcy8bw85g"
    }
}
```

**Example 2: 创建分配权重的 DNS 记录**

在 ZoneId 为 zone-225qgrnvbi9w 的站点下，创建一个记录名为 www.example.com，记录类型为 A，记录内容为1.2.3.4，缓存时间为60秒，记录权重为100的 DNS 记录。

Input: 

```
tccli teo CreateDnsRecord --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --Name www.example.com \
    --Type A \
    --Content 1.2.3.4 \
    --TTL 60 \
    --Weight 100
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "RecordId": "record-225rcy8bw85g"
    }
}
```

**Example 3: 创建分配解析线路的 DNS 记录**

在 ZoneId 为 zone-225qgrnvbi9w 的站点下，创建一个记录名为 www.example.com，记录类型为 A，解析线路为北京（CN.BJ），记录内容为1.2.3.4，缓存时间为60秒的 DNS 记录。

Input: 

```
tccli teo CreateDnsRecord --cli-unfold-argument  \
    --ZoneId zone-225qgrnvbi9w \
    --Name www.example.com \
    --Type A \
    --Location CN.BJ \
    --Content 1.2.3.4 \
    --TTL 60
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707",
        "RecordId": "record-225rcy8bw85g"
    }
}
```

