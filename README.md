# Investigation of the method of measuring the parameters of affine image transformation

### Example of work
> Source Images

<img src="https://user-images.githubusercontent.com/66872084/202682700-29271244-8275-4d1b-bb0d-a0c647354559.png" width="330"> <img src="https://user-images.githubusercontent.com/66872084/202682741-7a1eb8e5-d33c-4e95-ac75-5c1be17d07cb.png" width="330"> <img src="https://user-images.githubusercontent.com/66872084/202682759-563c76a7-a875-4073-965f-ee417293c9e8.png" width="330">

I get the threshold value of the image using the built-in OpenCV library function, using the THRESH_TOZERO method, an example of which is shown below.

> original image and TOZERO

<img src="https://user-images.githubusercontent.com/66872084/202683891-c119aa18-24e6-4732-b485-32d7ea44d035.png" width="100"> <img src="https://user-images.githubusercontent.com/66872084/202683914-bd9ffc83-81ba-47be-942e-2ced15f3cb1c.png" width="100">

Next, I'm looking for the coordinates of the central point of the figure in the original image using the moment function, also from the OpenCV library.

After the obtained values, I start looking for the original figure, for this I will initially find the abscissa and the ordinate of the pixels of the centered image. Having received the coordinates, I find the maststabbing coefficient and after that I can already find the affine coordinates. I get new images.

<img src="https://user-images.githubusercontent.com/66872084/202685577-a85c8d15-beef-4a02-88b5-4db3b6b90cc3.png" width="330"> <img src="https://user-images.githubusercontent.com/66872084/202685589-f012994f-4f2b-4f31-98ad-6104f7e861a1.png" width="330"> <img src="https://user-images.githubusercontent.com/66872084/202685600-f21bd0e2-87bb-4b25-9beb-c203a0f32821.png" width="330">

____

# Исследование метода измерения параметров аффинного преобразования изображений

Получаю пороговое значение изображения при помощи встроенной функции библиотеки OpenCV, использую при этом метод THRESH_TOZERO.
Ищу оригинальную фигуру, для этого первоначально найду абсциссу и ординату пикселей центрированного изображения. Получив координаты нахожу коэффицент мастштабирования и после этого смогу уже найти аффинные координаты.
