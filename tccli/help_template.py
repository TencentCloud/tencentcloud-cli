# -*- coding: utf-8 -*-
TCCLI_HELP = '''
NAME
        tccli

DESCRIPTION
        tccli (Tencent Cloud Command Line Interface) is a tool to manage your Tencent Cloud services.

CONFIGURE
        Before using tccli, you should use the command(tccli configure) to configure your profile as the default
        For more information, please enter tccli configure help

USEAGE
        tccli [options] <service> [options] <action> [options] [options and parameters]

OPTIONS
        help
        show the tccli help info

        version
        show the version of tccli

AVAILABLE SERVICES
%s
'''

CONFIGURE_HELP = '''
NAME
        configure

DESCRIPTION
        configure your profile(eg:secretId, secretKey, region, output).

USEAGE
        tccli configure [--profile profile-name]

OPTIONS
        help
        show the tccli configure help info

        --profile
        specify a profile name


AVAILABLE SUBCOMMAND
        get
        set
        list
'''

LIST_CONFIGURE = '''
NAME
        list

DESCRIPTION
        list your profile(eg:secretId, secretKey, region, output).

USEAGE
        tccli configure list [--profile profile-name]
        eg: tccli configure list

OPTIONS
        help
        show the tccli configure list help info

        --profile
        specify a profile name
'''

SET_CONFIGURE = '''
NAME
        set

DESCRIPTION
        set your profile(eg:secretId, secretKey, region, output).

USEAGE
        tccli configure set [CONFIG] [--profile profile-name]
        eg: tccli configure set Region ap-guangzhou

OPTIONS
        help
        show the tccli configure set help info

        --profile
        specify a profile name

AVAILABLE CONFIG
        secretId: TencentCloud API SecretId

        secretKey: TencentCloud API SecretKey

        region: which the region you want to work with belongs.

        output: TencentCloud API response format[json, text, table]

        [cvm, cbs ...].version: service [cvm cbs ...] version

        [cvm, cbs ...].endpoint: service [cvm cbs ...] access point domain name

'''


GET_CONFIGURE = '''
NAME
        get

DESCRIPTION
        get your profile(eg:SecretId, SecretKey, Region).

USEAGE
        tccli configure get [CONFIG] [--profile profile-name]
        eg: tccli configure get Region

OPTIONS
        help
        show the tccli configure get help info

        --profile
        specify a profile name

AVAILABLE CONFIG
        secretId: TencentCloud API SecretId

        secretKey: TencentCloud API SecretKey

        region: which the region you want to work with belongs.

        output: TencentCloud API response format[json, text, table]

        [cvm, cbs ...].version: service [cvm cbs ...] version

        [cvm, cbs ...].endpoint: service [cvm cbs ...] access point domain name
'''


SERVICE = '''
NAME
        %(name)s

DESCRIPTION
        %(desc)s

USEAGE
        tccli %(name)s <action> [--param...]

OPTIONS
        help
        show the tccli %(name)s help info

        --version
        specify a %(name)s api version

AVAILABLE ACTION
%(actions)s
'''

ACTION = '''
NAME
        %(name)s

DESCRIPTION
        %(desc)s

USEAGE
        tccli %(service)s %(name)s [--param...]

OPTIONS
        help
        show the tccli %(service)s %(name)s help info

        --profile
        specify a profile name

        --secretId
        specify a SecretId

        --secretKey
        specify a SecretKey

        --region
        identify the region to which the instance you want to work with belongs.

        --endpoint
        specify an access point domain name

        --version
        specify a %(name)s api version

        --filter
        specify a filter field

        --timeout
        specify a request timeout

AVAILABLE PARAMS
%(params)s
'''