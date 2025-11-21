# [Le Flocon - Chalet Reservation Website](https://le-flocon-677a64.eurecom.io/reservation.html)

**Le Flocon** is a responsive and modular reservation website designed for a seasonal rental chalet. The website enables users to view availability, explore the chalet, and book weeks directly through an interactive calendar integrated with Firebase Realtime Database.

## Features

- Multi-page static website (description, photos, map, FAQ, reservation)
- Calendar-based weekly reservation system (Saturday-to-Saturday)
- Real-time week availability and bookings stored in Firebase
- Season-based and multilingual content (summer/winter, French/English)
- Admin interface for managing reservations
- Lightweight and mobile-friendly front-end

## Technologies

- HTML5 / CSS3 / JavaScript 
- Firebase Realtime Database
- Leaflet.js (for the map)
- Flatpickr.js (for the calendar)
- Git / GitHub for source control

## Functional Overview

- **Calendar logic**: Using Flatpickr with Saturday-only selection and week-based filtering
- **Dynamic content**: Conditional HTML elements based on class names like `summer-only`, `winter-only`, or language-specific wrappers
- **Real-time booking**: Firebase is used to store weeks, prices, and confirmed reservations. The system prevents double bookings
- **Admin panel**: Allows the owner to view reservations, payment status, and total amounts

## Firebase Data Model

```json
reservations: {
  reservationId: {
    tenant: ...,
    total: ...,
    weeks: [...],
    payment: ...
  }
}
weeks: {
  "2025-06-06": {
    available: false,
    price: 233
  }
}
```