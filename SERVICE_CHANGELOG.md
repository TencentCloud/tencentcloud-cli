# Release 3.0.1319.1

## 云数据库 MySQL(cdb) 版本：2017-03-20

### 第 152 次发布

发布时间：2025-12-04 17:03:24

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDBInstanceProcess](http://document.tencentcloudapi.woa.com/document/product/236/88194)
* [DescribeInstancePasswordComplexity](http://document.tencentcloudapi.woa.com/document/product/236/88195)
* [KillDBProcessByIds](http://document.tencentcloudapi.woa.com/document/product/236/88193)
* [ModifyDBInstanceModes](http://document.tencentcloudapi.woa.com/document/product/236/88192)

修改接口：

* [AdjustCdbProxyAddress](http://document.tencentcloudapi.woa.com/document/product/236/77512)

	* 新增入参：ApNodeAsRoNode, ApQueryToOtherNode

* [CreateAccounts](http://document.tencentcloudapi.woa.com/document/product/236/17502)

	* 新增入参：SkipValidatePassword

* [CreateDBInstance](http://document.tencentcloudapi.woa.com/document/product/236/15871)

	* 新增入参：DiskEncryption, DestroyProtect

* [CreateDBInstanceHour](http://document.tencentcloudapi.woa.com/document/product/236/15865)

	* 新增入参：DiskEncryption, DestroyProtect

* [DescribeAccounts](http://document.tencentcloudapi.woa.com/document/product/236/17499)

	* 新增入参：SortBy, OrderBy

* [DescribeAuditConfig](http://document.tencentcloudapi.woa.com/document/product/236/45455)

	* 新增出参：IsOpening

* [ModifyAccountPassword](http://document.tencentcloudapi.woa.com/document/product/236/17497)

	* 新增入参：SkipValidatePassword

* [ModifyBackupEncryptionStatus](http://document.tencentcloudapi.woa.com/document/product/236/77063)

	* 新增入参：BinlogEncryptionStatus

* [OpenAuditService](http://document.tencentcloudapi.woa.com/document/product/236/75105)

	* 新增入参：IsTrial, SqlAnalyse

* [SwitchForUpgrade](http://document.tencentcloudapi.woa.com/document/product/236/15864)

	* 新增入参：IsRelatedSwitch


新增数据结构：

* [ProcessItem](http://document.tencentcloudapi.woa.com/document/product/236/15878#ProcessItem)

修改数据结构：

* [InstanceDbAuditStatus](http://document.tencentcloudapi.woa.com/document/product/236/15878#InstanceDbAuditStatus)

	* 新增成员：TrialStatus, TrialStartTime, TrialDuration, TrialCloseTime, TrialDescribeLogHours

* [InstanceInfo](http://document.tencentcloudapi.woa.com/document/product/236/15878#InstanceInfo)

	* 新增成员：DestroyProtect, DiskEncryption

* [ProxyAddress](http://document.tencentcloudapi.woa.com/document/product/236/15878#ProxyAddress)

	* 新增成员：ApNodeAsRoNode, ApQueryToOtherNode




## TDSQL-C MySQL 版(cynosdb) 版本：2019-01-07

### 第 146 次发布

发布时间：2025-12-04 01:13:40

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [ModifyClusterGlobalEncryption](http://document.tencentcloudapi.woa.com/document/product/1003/88182)



## 云数据库独享集群(dbdc) 版本：2020-10-29

### 第 2 次发布

发布时间：2025-12-04 01:14:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/1671/79405)

	* 新增出参：ResourceTags, CpuType


新增数据结构：

* [ResourceTag](http://document.tencentcloudapi.woa.com/document/product/1671/79408#ResourceTag)

修改数据结构：

* [DescribeInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/1671/79408#DescribeInstanceDetail)

	* 新增成员：ResourceTags, CpuType




## 数据传输服务(dts) 版本：2021-12-06

### 第 44 次发布

发布时间：2025-12-04 01:16:34

本次发布包含了以下内容：

改善已有的文档。

新增数据结构：

* [DBOpFilter](http://document.tencentcloudapi.woa.com/document/product/571/78340#DBOpFilter)
* [OpFilter](http://document.tencentcloudapi.woa.com/document/product/571/78340#OpFilter)
* [TableFilter](http://document.tencentcloudapi.woa.com/document/product/571/78340#TableFilter)
* [ViewFilter](http://document.tencentcloudapi.woa.com/document/product/571/78340#ViewFilter)

修改数据结构：

* [Objects](http://document.tencentcloudapi.woa.com/document/product/571/78340#Objects)

	* 新增成员：DatabasesOpFilter




## 数据传输服务(dts) 版本：2018-03-30



## Elasticsearch Service(es) 版本：2018-04-16

### 第 95 次发布

发布时间：2025-12-04 01:17:45

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [DescribeDbTknPwdRules](http://document.tencentcloudapi.woa.com/document/product/845/88185)
* [DescribeDbTknResource](http://document.tencentcloudapi.woa.com/document/product/845/88184)
* [ResetInstancePassword](http://document.tencentcloudapi.woa.com/document/product/845/88183)

新增数据结构：

* [Rules](http://document.tencentcloudapi.woa.com/document/product/845/30634#Rules)



## 密钥管理系统(kms) 版本：2019-01-18

### 第 12 次发布

发布时间：2025-12-04 01:22:10

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [GenerateDataKey](http://document.tencentcloudapi.woa.com/document/product/573/34419)

	* 新增入参：Tags

	* 新增出参：TagCode, TagMsg

* [ImportDataKey](http://document.tencentcloudapi.woa.com/document/product/573/87104)

	* 新增入参：Tags

	* 新增出参：TagCode, TagMsg

* [ListDataKeyDetail](http://document.tencentcloudapi.woa.com/document/product/573/87103)

	* 新增入参：TagFilters


修改数据结构：

* [DataKeyMetadata](http://document.tencentcloudapi.woa.com/document/product/573/34431#DataKeyMetadata)

	* 新增成员：KeyName




## 云数据库 MariaDB(mariadb) 版本：2017-03-12

### 第 53 次发布

发布时间：2025-12-04 01:22:54

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeDBInstanceDetail](http://document.tencentcloudapi.woa.com/document/product/237/77350)

	* 新增出参：FlowId




## 消息队列 MQTT 版(mqtt) 版本：2024-05-16

### 第 24 次发布

发布时间：2025-12-04 01:24:27

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateMessageEnrichmentRule](http://document.tencentcloudapi.woa.com/document/product/1773/88191)
* [DeleteMessageEnrichmentRule](http://document.tencentcloudapi.woa.com/document/product/1773/88190)
* [DescribeMessageEnrichmentRules](http://document.tencentcloudapi.woa.com/document/product/1773/88189)
* [ModifyMessageEnrichmentRule](http://document.tencentcloudapi.woa.com/document/product/1773/88188)
* [UpdateMessageEnrichmentRulePriority](http://document.tencentcloudapi.woa.com/document/product/1773/88187)

新增数据结构：

* [MessageEnrichmentRuleItem](http://document.tencentcloudapi.woa.com/document/product/1773/84898#MessageEnrichmentRuleItem)
* [MessageEnrichmentRulePriority](http://document.tencentcloudapi.woa.com/document/product/1773/84898#MessageEnrichmentRulePriority)



## API 安全测试模拟产品(secmocker) 版本：2024-07-18

### 第 2 次发布

发布时间：2025-12-04 01:27:08

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* MockNoAuthCommon



## 私有网络(vpc) 版本：2017-03-12

### 第 230 次发布

发布时间：2025-12-04 01:32:38

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreateNatGateway](http://document.tencentcloudapi.woa.com/document/product/215/36721)

	* 新增入参：ExclusiveType

* [ResetNatGatewayConnection](http://document.tencentcloudapi.woa.com/document/product/215/36713)

	* 新增入参：ExclusiveType


修改数据结构：

* [VpnGateway](http://document.tencentcloudapi.woa.com/document/product/215/15824#VpnGateway)

	* 新增成员：AssociationState




