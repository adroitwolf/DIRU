import service from '@/config/service'

const imageApi = {}

//  这边自定义api
imageApi.fuc1 = (file)=>{
    const formData = new FormData();
    formData.append("file", file);
    return service({
        url: `/func1`,
        headers: {
            'Content-Type': 'multipart/form-data'
        },
        data: formData,
        method: 'post',
    })
}

imageApi.fitler = (file,arg)=>{
    console.log(file)
    console.log(arg)
    const formData = new FormData();
    formData.append("file", file);
    formData.append("filter",arg);
    return service({
        url:`/filter`,
        headers: {
            'Content-Type': 'multipart/form-data'
        },
        data: formData,
        method: 'post',
    })
}

export default imageApi