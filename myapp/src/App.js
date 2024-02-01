import React, { useState, useEffect } from 'react';
import FileTree from './FileTree';

const App = () => {
  const [fileTreeData, setFileTreeData] = useState(null);

  useEffect(() => {
    fetch('/api/customer') // Fetch data from the backend API
      .then(response => response.json())
      .then(data => setFileTreeData(data))
      .catch(error => console.error('Error fetching file tree data:', error));
  }, []);

  return (
    <div>
      <h1>File Tree App</h1>
      {fileTreeData && <FileTree data={fileTreeData} />}
    </div>
  );
};

export default App;
