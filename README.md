# Final Assignment

### Status

Once you are finished with the final assignment, edit this readme and add "x" to the correct box:

* [x] Submitted

* [ ] I'm still working on my final assignment. 


## Topic: Unobstructed pedestrian routes in Helsinki center

### Input data: Esteettömyysaineistot exel-taulukoina from the city of Helsinki. (Lähtötiedot)

### Analysis steps:

1. I received the data of unbstructed routes, areas and voice signaled traffic lights from the city of Helsinki via my collegue. 
2. Then I studied the data and made small modifications like changing th crs, to be able to unify and join the separate tables.
3. I filtered the data using a bounding box inside city center area so that I can test the methods faster and because the unobstructed areas were more dense there.
4. I made buffers of the unobstructed routes and areas to be able to make spatial analysis.
5. I joined the buffers.
6. I created folium maps to show the data on an interactive map.
7. I made analysis of shortest paths, between two given addressses and visualized the obstructedness of the route by using spatial analysis.
8. And finally saved an html map with the route between two given addresses. 

### Results:
[Esteettömyyskartta](https://autogis-2019.github.io/final-assignment-vipy123/Esteetomyyskartta1.html) of Helsinki city center unobstructed routes and areas and [reittikartta](https://autogis-2019.github.io/final-assignment-vipy123/valitulostus1.html), that shows the shortest path between two addresses. The unbstructed parts of the route are highlighted with green and obstructed routes with red. 
The idea was to create my own dijkstra algorithme by using a weighted vector lenghts between nodes. I also wanted to make a small webapp that would have enabled unobstructed route planning with origin and destination addresses, but I ran out of time. also jupyter lab stopped working on the last evening. These ideas can be developed later though.