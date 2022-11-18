import axios from 'axios'

// 创建axios实例
var service = axios.create({
    timeout: 1000 * 12,
    baseURL: "http://127.0.0.1:5000"
});
// 拦截器
service.interceptors.request.use(
    config => {
        return config;
    },
    error => Promise.error(error)
)



export default service