**Example 1: 批量修改指定记录 ID 的 DNS 记录**

在 ZoneId 为 zone-225qgrnvbi9w 的站点下，将记录 ID 为 record-3d5dg39c 的 DNS 记录的记录名改成 eo-test1.com，记录类型改成 CNAME，记录内容改成 eo-test1.c4games.com.eo.dnse2.com；将记录 ID 为 record-gkd9gyrv 的 DNS 记录的记录名改成 eo-test2.com，记录类型改成 A，记录内容改成 1.2.3.4。

Input: 

```
tccli teo ModifyDnsRecords --cli-unfold-argument  \
    --DnsRecords.0.RecordId record-3d5dg39c \
    --DnsRecords.0.Name eo-test1.com \
    --DnsRecords.0.Type CNAME \
    --DnsRecords.0.Content eo-test1.c4games.com.eo.dnse2.com \
    --DnsRecords.1.RecordId record-gkd9gyrv \
    --DnsRecords.1.Name eo-test2.com \
    --DnsRecords.1.Type A \
    --DnsRecords.1.Content 1.2.3.4 \
    --ZoneId zone-20hzkd4rdmy0
```

Output: 
```
{
    "Response": {
        "RequestId": "d08bed0d-15bf-4d65-ab56-906aee0c845"
    }
}
```

**Example 2: 批量修改指定记录 ID 的 DNS 记录的记录权重**

在 ZoneId 为 zone-225qgrnvbi9w 的站点下，将记录 ID 为 record-3d5dg39c 的 DNS 记录的记录权重改成40；将记录 ID 为 record-gkd9gyrv 的 DNS 记录的记录权重改成60。

Input: 

```
tccli teo ModifyDnsRecords --cli-unfold-argument  \
    --DnsRecords.0.RecordId record-3d5dg39c \
    --DnsRecords.0.Weight 40 \
    --DnsRecords.1.RecordId record-gkd9gyrv \
    --DnsRecords.1.Weight 60 \
    --ZoneId zone-20hzkd4rdmy0
```

Output: 
```
{
    "Response": {
        "RequestId": "d08bed0d-15bf-4d65-ab56-906aee0c845"
    }
}
```

**Example 3: 批量修改指定记录 ID 的 DNS 记录的解析线路和记录内容**

在 ZoneId 为 zone-225qgrnvbi9w 的站点下，将记录 ID 为 record-3d5dg39c 的 DNS 记录的记录解析线路改成北京（CN.BJ），记录内容改成 eo-test1.c4games.com.eo.dnse2.com；将记录 ID 为 record-gkd9gyrv 的 DNS 记录的记录解析线路改成福建（CN.FJ），记录内容改成 eo-test2.c4games.com.eo.dnse2.com。

Input: 

```
tccli teo ModifyDnsRecords --cli-unfold-argument  \
    --DnsRecords.0.RecordId record-3d5dg39c \
    --DnsRecords.0.Location CN.BJ \
    --DnsRecords.0.Content eo-test1.c4games.com.eo.dnse2.com \
    --DnsRecords.1.RecordId record-gkd9gyrv \
    --DnsRecords.1.Location CN.FJ \
    --DnsRecords.1.Content eo-test2.c4games.com.eo.dnse2.com \
    --ZoneId zone-20hzkd4rdmy0
```

Output: 
```
{
    "Response": {
        "RequestId": "d08bed0d-15bf-4d65-ab56-906aee0c845"
    }
}
```

