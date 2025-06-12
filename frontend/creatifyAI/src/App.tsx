import React, { useState } from 'react';

function App() {
  const [url, setUrl] = useState<string>('');
  const [videoUrl, setVideoUrl] = useState<string>('');

  const handleSubmit = async (): Promise<void> => {
    const formData = new FormData();
    formData.append('url', url);
    const res = await fetch('http://localhost:8000/generate', {
      method: 'POST',
      body: formData,
    });
    const data = await res.json();
    const fullVideoUrl = `http://localhost:8000/videos/${data.video_url}`;
    setVideoUrl(fullVideoUrl);
  };

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold mb-4">URL to Video Generator</h1>
      <br></br>
      <br></br>
      <input
        className="border p-2 w-full"
        value={url}
        onChange={(e: React.ChangeEvent<HTMLInputElement>) => setUrl(e.target.value)}
        placeholder="Enter product URL"
      />
      <br></br>
      <br></br>
      <button
        className="bg-blue-500 text-white px-4 py-2 mt-2"
        onClick={handleSubmit}
      >
        Generate
      </button>
      <br></br>
      <br></br>
      {videoUrl && <video className="mt-4" src={videoUrl} controls width="480" />}
      <br></br>
      <br></br>
      {videoUrl && <p className="mt-2">Video generated successfully!</p>}
      <br></br>
      <br></br>
      {videoUrl && <a href={videoUrl} className="text-blue-500 mt-2 block">Download Video</a>}
    </div>
  );
}

export default App;