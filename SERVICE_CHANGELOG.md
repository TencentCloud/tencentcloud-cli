# Release 3.0.1383.1

## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 155 次发布

发布时间：2026-03-16 01:29:35

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyServerlessStrategy](http://document.tencentcloudapi.woa.com/document/product/1003/84781)

	* 新增入参：SecurityGroupIdsForNewRo


新增数据结构：

* [CreateBackupVaultItem](http://document.tencentcloudapi.woa.com/document/product/1003/48097#CreateBackupVaultItem)
* [VaultInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#VaultInfo)

修改数据结构：

* [BackupConfigInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BackupConfigInfo)

	* 新增成员：AutoCopyVaults

* [BackupFileInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BackupFileInfo)

	* 新增成员：CopyStatus, EncryptKeyId, EncryptRegion, VaultInfos

* [BinlogConfigInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BinlogConfigInfo)

	* 新增成员：AutoCopyVaults

* [BinlogItem](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BinlogItem)

	* 新增成员：CopyStatus, VaultInfos, EncryptKeyId, EncryptRegion

* [BizTaskInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#BizTaskInfo)

	* 新增成员：VaultId, VaultName

* [LogicBackupConfigInfo](http://document.tencentcloudapi.woa.com/document/product/1003/48097#LogicBackupConfigInfo)

	* 新增成员：AutoCopyVaults

* [RedoLogItem](http://document.tencentcloudapi.woa.com/document/product/1003/48097#RedoLogItem)

	* 新增成员：VaultInfos, CopyStatus, EncryptKeyId, EncryptRegion

* [SnapshotBackupConfig](http://document.tencentcloudapi.woa.com/document/product/1003/48097#SnapshotBackupConfig)

	* 新增成员：AutoCopyVaults




## Elasticsearch Service(es) 版本：2018-04-16

### 第 103 次发布

发布时间：2026-03-16 01:40:23

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CheckOperation](http://document.tencentcloudapi.woa.com/document/product/845/83434)

	* 新增出参：AbnormalNodes


新增数据结构：

* [NodeDetail](http://document.tencentcloudapi.woa.com/document/product/845/30634#NodeDetail)



## 边缘安全加速平台(teo) 版本：2022-09-01

### 第 72 次发布

发布时间：2026-03-16 02:17:20

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [EnableOriginACL](http://document.tencentcloudapi.woa.com/document/product/1738/87123)

	* 新增入参：OriginACLFamily

* [ModifyOriginACL](http://document.tencentcloudapi.woa.com/document/product/1738/87122)

	* 新增入参：OriginACLFamily


修改数据结构：

* [OriginACLInfo](http://document.tencentcloudapi.woa.com/document/product/1738/81211#OriginACLInfo)

	* 新增成员：OriginACLFamily




## 边缘安全加速平台(teo) 版本：2022-01-06



