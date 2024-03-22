import React, {useState} from 'react';
import axios from 'axios';

function FileUploadPage({setIsSubmitted, setData}){
	const [selectedFile, setSelectedFile] = useState();
	const [isFilePicked, setIsFilePicked] = useState(false);

	const changeHandler = (event) => {
		setSelectedFile(event.target.files[0]);
		setIsFilePicked(true);
	};

	const handleSubmission = () => {
        const data = new FormData() 
        data.append('files', selectedFile)
        axios.post(`/api/v1/forecast?nb_days=365`, data, {
            })
            .then(res => {
                setData(res.data);
                setIsSubmitted(true);
        })
        
	};

	return(
   <div className='mx-auto mt-8 w-96 border-blue-700 border-2 p-4 rounded-lg'>
	<h1 className='text-center mb-4 text-base font-bold'>Prophet model UI interface</h1>
        <label>
            <input type="file" className="text-sm text-grey-500
            file:mr-5 file:py-2 file:px-6
            file:rounded-full file:border-0
            file:text-sm file:font-medium
            file:bg-blue-50 file:text-blue-700
            hover:file:cursor-pointer" name="file" onChange={changeHandler} />
		{isFilePicked ? (
					<div className='text-center mb-4'>
					{selectedFile.type === 'text/csv' ? (
						<p></p>
					) : (
						<p>This is not a CSV file!</p>
					)}
					</div>
				) : (
					<p className='text-center mb-4'></p>
				)}
        </label>
        <div className="h-6"></div>
			<label htmlFor="last_name" className="block my-4 text-sm font-medium ">Number of days to forcast</label>
            <input type="number" id="nb_days" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="365" required></input>
			<div className='flex justify-center'>
				<button onClick={handleSubmission} className="bg-blue-50 mt-4 rounded-full text-blue-700 py-2 px-4">Submit</button>
			</div>
		</div>
	)
}

export default FileUploadPage;