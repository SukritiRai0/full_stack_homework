import React from 'react';

const FileTree = ({ data }) => {
  return (
    <ul>
      {data.map((item, index) => (
        <li key={index}>
          <span>{item.name}</span>
          {item.parts && <FileTree data={item.parts} />}
          {item.revisions && <FileTree data={item.revisions} />}
          {item.trials && <FileTree data={item.trials} />}
          {item.files && (
            <ul>
              {item.files.map((file, fileIndex) => (
                <li key={fileIndex}>
                  <span>📄 {file.name}</span>
                </li>
              ))}
            </ul>
          )}
        </li>
      ))}
    </ul>
  );
};

export default FileTree;
