# Stale Bus Detector

## Demo: https://www.linkedin.com/posts/md-intikhab-shahriar-hasan-143925169_dataabranalytics-dataabrengineering-infotactabrsolutions-activity-7368964714871128064-WxgI?utm_source=share&utm_medium=member_desktop&rcm=ACoAACgugIMBxbp9aesalLcUsSorWs_BtzxNjX0

We're happy to share with you the progress of our internship project at Infotact Solutions, where we're assigned to develop a 'Real-Time Stale-Bus Detector' data analytics engine with the help of a React app. 

We've made the app with TransLink's GTFS-RT feed for Australia, mainly its transit information for the cities Brisbane, Gold Coast, and Sunshine Coast. 

Problem Statement: To develop a real-time analytics system that identifies "ghost buses" in a public transit network—vehicles that appear on tracking apps but are not in service, are non-responsive, or are severely off-route—to provide riders with a more accurate and reliable view of the transit system.

The objectives and deliverables of the project were - 

• Develop a data pipeline to ingest and parse GTFS-Realtime data from a city's transit authority.
• Build an analytics engine to detect anomalies like stale GPS data, non-movement, and significant route deviations.  
• Create a live map dashboard that visually distinguishes reliable buses from "Stale/Stationary" buses. 

On doing so, we've flagged all Active buses with green markers and all Stale/Stationary buses with red markers on the map, with a tooltip of the reason for their being flagged red. Besides, the user can hide red-flagged buses from the map to get information about active buses only. 

The project is containerized with the help of a Docker image and deployed at Render for live usability.
