// fileTreeData.js
const fileTreeData = {
    customers: [
      {
        name: 'Sukriti',
        isDirectory: true,
        parts: [
          {
            name: 'Hat',
            isDirectory: true,
            revisions: [
              {
                name: 'Revision 1',
                isDirectory: true,
                files: [
                  { name: 'file1.txt', isDirectory: false },
                ],
              },
              // More revisions...
            ],
            trials: [
              {
                name: 'Trial 1',
                isDirectory: true,
                files: [
                  { name: 'file3.txt', isDirectory: false },
                ],
              },
              // More trials...
            ],
          },
          {
            name: 'Flange',
            isDirectory: true,
            revisions: [
              {
                name: 'Revision 1',
                isDirectory: true,
                files: [
                  { name: 'file1.txt', isDirectory: false },
                ],
              },
              // More revisions...
            ],
            trials: [
              {
                name: 'Trial 1',
                isDirectory: true,
                files: [
                  { name: 'file3.txt', isDirectory: false },
                ],
              },
              // More trials...
            ],
          }
          // More parts...
        ],
      },
      {
        name: 'Customer 2',
        isDirectory: true,
        parts: [
          {
            name: 'Hat',
            isDirectory: true,
            revisions: [
              {
                name: 'Revision 1',
                isDirectory: true,
                files: [
                  { name: 'file1.txt', isDirectory: false },
                  { name: 'file2.csv', isDirectory: false },
                ],
              },
              // More revisions...
            ],
            trials: [
              {
                name: 'Trial 1',
                isDirectory: true,
                files: [
                  { name: 'file3.txt', isDirectory: false },
                  { name: 'file4.step', isDirectory: false },
                ],
              },
              // More trials...
            ],
          },
          // More parts...
        ],
      }
      // More customers...
    ],
    
  };
  
  export default fileTreeData;  