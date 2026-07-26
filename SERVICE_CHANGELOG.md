# Release 3.0.1462.1

## 腾讯云智能体开发平台(adp) 版本：2026-05-20

### 第 8 次发布

发布时间：2026-07-27 01:07:35

本次发布包含了以下内容：

改善已有的文档。

新增接口：

* [CreateAppTrigger](http://document.tencentcloudapi.woa.com/document/product/1815/91989)
* [CreateTimerTask](http://document.tencentcloudapi.woa.com/document/product/1815/91988)
* [DeleteAppTrigger](http://document.tencentcloudapi.woa.com/document/product/1815/91987)
* [DeleteTimerTask](http://document.tencentcloudapi.woa.com/document/product/1815/91986)
* [DescribeAppTrigger](http://document.tencentcloudapi.woa.com/document/product/1815/91985)
* [DescribeAppTriggerInstance](http://document.tencentcloudapi.woa.com/document/product/1815/91984)
* [DescribeAppTriggerRunLogList](http://document.tencentcloudapi.woa.com/document/product/1815/91983)
* [DescribeAppTriggerSummaryList](http://document.tencentcloudapi.woa.com/document/product/1815/91982)
* [DescribeTimerTask](http://document.tencentcloudapi.woa.com/document/product/1815/91981)
* [DescribeTimerTaskRunLogList](http://document.tencentcloudapi.woa.com/document/product/1815/91980)
* [DescribeTimerTaskSummaryList](http://document.tencentcloudapi.woa.com/document/product/1815/91979)
* [MarkAppTriggerRunLogRead](http://document.tencentcloudapi.woa.com/document/product/1815/91978)
* [MarkTimerTaskRunLogRead](http://document.tencentcloudapi.woa.com/document/product/1815/91977)
* [ModifyAppTrigger](http://document.tencentcloudapi.woa.com/document/product/1815/91976)
* [ModifyTimerTask](http://document.tencentcloudapi.woa.com/document/product/1815/91975)
* [PauseAppTrigger](http://document.tencentcloudapi.woa.com/document/product/1815/91974)
* [PauseTimerTask](http://document.tencentcloudapi.woa.com/document/product/1815/91973)
* [ResumeAppTrigger](http://document.tencentcloudapi.woa.com/document/product/1815/91972)
* [ResumeTimerTask](http://document.tencentcloudapi.woa.com/document/product/1815/91971)
* [RunAppTriggerNow](http://document.tencentcloudapi.woa.com/document/product/1815/91970)
* [RunTimerTaskNow](http://document.tencentcloudapi.woa.com/document/product/1815/91969)

新增数据结构：

* [AppTrigger](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTrigger)
* [AppTriggerInstance](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerInstance)
* [AppTriggerParamBinding](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerParamBinding)
* [AppTriggerParamBindingConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerParamBindingConfig)
* [AppTriggerParamBindingValue](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerParamBindingValue)
* [AppTriggerParamSchema](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerParamSchema)
* [AppTriggerPromptExecuteConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerPromptExecuteConfig)
* [AppTriggerRunLog](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerRunLog)
* [AppTriggerScheduleConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerScheduleConfig)
* [AppTriggerScheduleStatus](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerScheduleStatus)
* [AppTriggerSummary](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerSummary)
* [AppTriggerWebhookConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerWebhookConfig)
* [AppTriggerWebhookParamSchemaConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerWebhookParamSchemaConfig)
* [AppTriggerWebhookStatus](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerWebhookStatus)
* [AppTriggerWorkflowExecuteConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#AppTriggerWorkflowExecuteConfig)
* [CronSchedule](http://document.tencentcloudapi.woa.com/document/product/1815/91428#CronSchedule)
* [DailySchedule](http://document.tencentcloudapi.woa.com/document/product/1815/91428#DailySchedule)
* [ExecuteConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#ExecuteConfig)
* [IntervalSchedule](http://document.tencentcloudapi.woa.com/document/product/1815/91428#IntervalSchedule)
* [ManualOnlySchedule](http://document.tencentcloudapi.woa.com/document/product/1815/91428#ManualOnlySchedule)
* [OnceSchedule](http://document.tencentcloudapi.woa.com/document/product/1815/91428#OnceSchedule)
* [TimerConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TimerConfig)
* [TimerProfile](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TimerProfile)
* [TimerPushConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TimerPushConfig)
* [TimerScheduleConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TimerScheduleConfig)
* [TimerStatus](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TimerStatus)
* [TimerTask](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TimerTask)
* [TimerTaskSummary](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TimerTaskSummary)
* [TriggerConfig](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TriggerConfig)
* [TriggerStatus](http://document.tencentcloudapi.woa.com/document/product/1815/91428#TriggerStatus)
* [WeeklySchedule](http://document.tencentcloudapi.woa.com/document/product/1815/91428#WeeklySchedule)
* [WeeklyTime](http://document.tencentcloudapi.woa.com/document/product/1815/91428#WeeklyTime)



## 云防火墙(cfw) 版本：2019-09-04

### 第 106 次发布

发布时间：2026-07-27 01:25:37

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [DeleteBlockIgnoreRuleNew](http://document.tencentcloudapi.woa.com/document/product/1132/83373)

	* <font color="#dd0000">**修改入参**：</font>ShowType




## 腾讯电子签（基础版）(essbasic) 版本：2021-05-26

### 第 236 次发布

发布时间：2026-07-27 01:49:20

本次发布包含了以下内容：

改善已有的文档。

修改接口：

* [ModifyPartnerAutoSignAuthUrl](http://document.tencentcloudapi.woa.com/document/product/1595/87083)

	* 新增入参：SealTypes




## 腾讯电子签（基础版）(essbasic) 版本：2020-12-22



