**Example 1: demo**



Input: 

```
tccli wedata UpdateConnection --cli-unfold-argument  \
    --WorkspaceId aa-zz \
    --Connection.ConnectionId 7d66d26b-0bac-475f-9307-f2cc20665053 \
    --Connection.ConnectionName hive_kerberos51 \
    --Connection.DisplayName hive_kerberos \
    --Connection.ConnectionType hive \
    --Connection.AuthType kerberos \
    --Connection.ConnectionDetail {"url":"jdbc:hive2://30.46.13.13:1784/default","principal":"ccc","principal1":"ccc"} \
    --Connection.FileCosInfo.CosRegion ap-beijing \
    --Connection.FileCosInfo.CosBucket abeltest \
    --Connection.FileList.0.FileName keytab3 \
    --Connection.FileList.0.FilePath /a/aa/aa \
    --Connection.FileList.0.FileDetail tt \
    --Connection.FileList.1.FileName kyb5.conf \
    --Connection.FileList.1.FilePath /a/ab/ab \
    --Connection.FileList.1.FileDetail tt \
    --Connection.FileList.2.FileName core-site.xml \
    --Connection.FileList.2.FilePath /a/a/a \
    --Connection.FileList.2.FileDetail tt \
    --Connection.FileList.3.FileName hdfs-site.xml \
    --Connection.FileList.3.FilePath /a/b/b \
    --Connection.FileList.3.FileDetail tt \
    --Connection.FileList.4.FileName hive-site.xml \
    --Connection.FileList.4.FilePath /a/c/c \
    --Connection.FileList.4.FileDetail tt
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "baafb044-492a-4ce9-a102-13b8a26ef249"
    }
}
```

