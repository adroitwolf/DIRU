import service from '@/config/service'

const imageApi = {}

imageApi.fuc1 = (file)=>{
    const formData = new FormData();
    formData.append("file", file);
    return service({
        url: `/func1`,
        headers: {
            'Content-Type': 'multipart/form-data'
        },
        data: formData,
        method: 'post'

    })
}

export default imageApi