**Example 1: URL刷新**

此清除类型使用的是直接删除的清除方法，会匹配清除提交的 URL 的节点缓存资源。
例如：需要清除站点域名 www.example.com 下 /a.txt 资源，可以参照以下示例进行刷新。



Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Targets http://www.example.com/a.txt \
    --Type purge_url \
    --ZoneId zone-ajj243dwrew
```

Output: 
```
{
    "Response": {
        "JobId": "20ga521cpwch",
        "FailedList": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: Hostname 刷新**

此清除类型使用的是标记过期的清除方法，会将提交的 Hostname 下的所有资源标记为过期。
例如：需要清除站点域名 www.example.com 下所有发生过变更的资源，可以参照以下示例进行刷新。<li>注意：不支持提交 *.test.com 格式的 Host，即域名中不能包含通配符，需要写明对应的子域名。</li>

Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Targets www.example.com \
    --Type purge_host \
    --ZoneId zone-ajj243dwrew
```

Output: 
```
{
    "Response": {
        "JobId": "20ga521cpwcs",
        "FailedList": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 3: Cache-Tag 刷新**

此清除类型使用的是直接清除的清除方法，会将该站点下所有 HTTP 应答包中存在对应 Cache-Tag 响应头标签值（tags）的资源直接清除。
例如：需要清除站点 example.com 下所有 HTTP 应答包中包含 tag1、tag2 或 tag3 标签的资源，可以参照以下示例进行刷新。

Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Targets tag1 tag2 tag3 \
    --Type purge_cache_tag \
    --ZoneId zone-ajj243dwrew
```

Output: 
```
{
    "Response": {
        "JobId": "20ga521cpwcs",
        "FailedList": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 4: 刷新站点下全部缓存**

此清除类型使用的是标记过期的清除方法，会将所提交站点下的缓存内容都标记为过期。
例如：需要清除站点 example.com 下的所有发生过变更的资源，可以参考以下示例进行刷新。

Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Type purge_all \
    --ZoneId zone-ajj243dwrew
```

Output: 
```
{
    "Response": {
        "JobId": "20ga521cpwcs",
        "FailedList": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 5: 目录刷新 — 直接删除对应目录下的资源**

此清除方式需要将 Method 的值调整为 delete， 使用直接删除的清除方法清除节点资源。
例如：需要清除站点域名 www.example.com 下 /test 目录下所有资源，可以参考以下示例进行刷新。


Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Targets http://www.example.com/test/ \
    --Type purge_prefix \
    --Method delete \
    --ZoneId zone-ajj243dwrew
```

Output: 
```
{
    "Response": {
        "JobId": "20ga521cpwck",
        "FailedList": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 6: 目录刷新 — 仅刷新目录下发生变更的资源**

此清除类型默认使用的是标记过期的清除方法，可以根据 Method 调整清除方式。
例如：需要清除站点域名 www.example.com 下 /test 目录下所有发生变更的资源，可以参考以下示例进行刷新。


Input: 

```
tccli teo CreatePurgeTask --cli-unfold-argument  \
    --Targets http://www.example.com/test/ \
    --Type purge_prefix \
    --Method invalidate \
    --ZoneId zone-ajj243dwrew
```

Output: 
```
{
    "Response": {
        "JobId": "20ga521cpwcj",
        "FailedList": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

