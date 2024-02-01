import React from 'react';
import FileTree from './FileTree';
import fileTreeData from './fileTreeData'; // Adjust the path accordingly

const App = () => {
  return (
    <div>
      <h1>File Tree App</h1>
      <FileTree data={fileTreeData.customers} />
    </div>
  );
};

export default App;