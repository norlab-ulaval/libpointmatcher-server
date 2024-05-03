import { getFiles } from '@/api'

export let files = {};

export const loadFiles = async () => {
    const response = await getFiles();
    if (response.success) {
        files = response.files;
    } else {
        console.error(response.error);
    }
}