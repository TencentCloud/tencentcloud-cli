# Release 3.0.1460.1

## Agent 沙箱服务(ags) 版本：2025-09-20

### 第 20 次发布

发布时间：2026-07-23 01:08:58

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [CreatePreCacheImageTask](http://document.tencentcloudapi.woa.com/document/product/1804/88713)

	* 新增入参：ImageRegistryConfig

	* <font color="#dd0000">**删除入参**：</font>ImageRegistryCredentialProviderId

* [DescribePreCacheImageTask](http://document.tencentcloudapi.woa.com/document/product/1804/88712)

	* 新增入参：ImageRegistryConfig, Scopes

	* 新增出参：Scopes

* [StartSandboxInstance](http://document.tencentcloudapi.woa.com/document/product/1804/87847)

	* 新增入参：StorageMounts


新增数据结构：

* [ImageRegistryConfig](http://document.tencentcloudapi.woa.com/document/product/1804/87854#ImageRegistryConfig)
* [ImageRegistryNetworkConfig](http://document.tencentcloudapi.woa.com/document/product/1804/87854#ImageRegistryNetworkConfig)

修改数据结构：

* [CustomConfiguration](http://document.tencentcloudapi.woa.com/document/product/1804/87854#CustomConfiguration)

	* 新增成员：ImageRegistryConfig

* [CustomConfigurationDetail](http://document.tencentcloudapi.woa.com/document/product/1804/87854#CustomConfigurationDetail)

	* 新增成员：ImageRegistryConfig

* [SandboxInstance](http://document.tencentcloudapi.woa.com/document/product/1804/87854#SandboxInstance)

	* 新增成员：StorageMounts




## 云 HDFS(chdfs) 版本：2020-11-12

### 第 10 次发布

发布时间：2026-07-23 01:26:58

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreatePathProtectionRule](http://document.tencentcloudapi.woa.com/document/product/1105/91881)
* [DeletePathProtectionRule](http://document.tencentcloudapi.woa.com/document/product/1105/91880)
* [DescribePathProtectionRules](http://document.tencentcloudapi.woa.com/document/product/1105/91879)
* [ModifyPathProtectionRule](http://document.tencentcloudapi.woa.com/document/product/1105/91878)

新增数据结构：

* [PathProtectionRule](http://document.tencentcloudapi.woa.com/document/product/1105/51158#PathProtectionRule)



## 云 HDFS(chdfs) 版本：2019-07-18



## 数据湖计算 DLC(dlc) 版本：2021-01-25

### 第 163 次发布

发布时间：2026-07-23 01:41:17

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [AlterTableComment](http://document.tencentcloudapi.woa.com/document/product/1342/91883)
* [DeleteMetaDatabase](http://document.tencentcloudapi.woa.com/document/product/1342/91885)
* [DescribeDatabase](http://document.tencentcloudapi.woa.com/document/product/1342/91884)
* [GenerateInternalTable](http://document.tencentcloudapi.woa.com/document/product/1342/91882)



## iOA 零信任安全管理系统(ioa) 版本：2022-06-01

### 第 44 次发布

发布时间：2026-07-23 01:58:24

本次发布包含了以下内容：

改善已有的文档。

<font color="#dd0000">**预下线接口**：</font>

* DescribeDeviceDetailList



## 凭据管理系统(ssm) 版本：2019-09-23

### 第 19 次发布

发布时间：2026-07-23 02:22:37

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeleteSecret](http://document.tencentcloudapi.woa.com/document/product/1140/40528)

	* 新增入参：DeleteMode

	* 新增出参：FlowID

* [DescribeRotationHistory](http://document.tencentcloudapi.woa.com/document/product/1140/58263)

	* 新增出参：AccountInfoList

* [DescribeSecret](http://document.tencentcloudapi.woa.com/document/product/1140/40526)

	* 新增出参：AccountInfoList


新增数据结构：

* [SecretAccountInfo](http://document.tencentcloudapi.woa.com/document/product/1140/40530#SecretAccountInfo)



## TI-ONE 训练平台(tione) 版本：2021-11-11

### 第 144 次发布

发布时间：2026-07-23 02:32:43

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DescribeModelService](http://document.tencentcloudapi.woa.com/document/product/851/76496)

	* 新增入参：TiProjectId

* [DescribeModelServiceGroup](http://document.tencentcloudapi.woa.com/document/product/851/76494)

	* 新增入参：TiProjectId

* [DescribeModelServices](http://document.tencentcloudapi.woa.com/document/product/851/76490)

	* 新增入参：TiProjectId


修改数据结构：

* [ImageCacheSourceInfo](http://document.tencentcloudapi.woa.com/document/product/851/74915#ImageCacheSourceInfo)

	* 新增成员：KeyId




## TI-ONE 训练平台(tione) 版本：2019-10-22



