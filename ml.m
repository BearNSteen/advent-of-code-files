% Specify the folder containing the images
folder = 'C:\path\to\images';

% Get all the image files in the folder
imageFiles = dir(fullfile(folder, '*.jpg'));

% Create a figure window
figure;

% Loop through each image file and plot it in the figure window
for i = 1:length(imageFiles)
  % Read the image file
  image = imread(fullfile(folder, imageFiles(i).name));

  % Plot the image
  imshow(image);

  % Pause for a short time to allow the user to see the image
  pause(0.5);
end