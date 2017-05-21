
exception ExceptionError {
    1: required i32 err_no,
    2: required string err_msg,
}

struct TaskReq {
    1: string url,
}


struct TaskResponse {
    1: required i32 code,
    2: required string message,
}


# 接受任务推送
service TaskService {
   TaskResponse add_task(1: TaskReq req);
}
