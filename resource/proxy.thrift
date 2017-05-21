exception ExceptionError {
    1: required i32 err_no,
    2: required string err_msg,
}

struct ProxyReq {
    1: string url,
}

struct Proxy {
    1: string url
}



# 接受任务推送
service ProxyService {
   Proxy get_proxy(1: ProxyReq req) throws (1: ExceptionError ex);
}
