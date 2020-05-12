test_data=[
    {"mobile":"","pwd":"","expected":"请输入手机号"},
    {"mobile":"123","pwd":"","expected":"请输入正确的手机号"}
]

test_data_success = [
    {"mobile": "18684720553", "pwd": "python", "expected": "我的帐户[python]"}
    ]

test_data_not_invalid = [
    {"mobile": "15746732896", "pwd": "123", "expected": "此账号没有经过授权，请联系管理员!"}
]