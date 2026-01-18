/* =========================================================
   APPOINTMENT BOOKING APP – FULL DDL (MySQL / Aurora MySQL)
   Includes: created_at, updated_at, deleted_at (soft delete)
   ========================================================= */

SET FOREIGN_KEY_CHECKS = 0;

/* =========================
   1. USERS
   ========================= */
CREATE TABLE users (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    role ENUM('ADMIN', 'PHYSICIAN', 'PATIENT', 'STAFF') NOT NULL,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone VARCHAR(20),
    password_hash VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    mfa_hash VARCHAR(255),
    mfa_enabled BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL
);

/* =========================
   2. PHYSICIANS
   ========================= */
CREATE TABLE physicians (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT UNIQUE,
    specialization VARCHAR(150),
    experience_years INT,
    license_number VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,

    CONSTRAINT fk_physicians_user
        FOREIGN KEY (user_id) REFERENCES users(id)
);

/* =========================
   3. LOCATIONS
   ========================= */
CREATE TABLE locations (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    postal_code VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL
);

/* =========================
   4. PHYSICIAN_LOCATIONS
   ========================= */
CREATE TABLE physician_locations (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    physician_id BIGINT NOT NULL,
    location_id BIGINT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,

    CONSTRAINT fk_pl_physician
        FOREIGN KEY (physician_id) REFERENCES physicians(id),

    CONSTRAINT fk_pl_location
        FOREIGN KEY (location_id) REFERENCES locations(id),

    UNIQUE (physician_id, location_id)
);

/* =========================
   5. PATIENTS
   ========================= */
CREATE TABLE patients (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT,
    full_name VARCHAR(150) NOT NULL,
    dob DATE,
    gender ENUM('MALE', 'FEMALE', 'OTHER'),
    phone VARCHAR(20),
    email VARCHAR(150),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,

    CONSTRAINT fk_patients_user
        FOREIGN KEY (user_id) REFERENCES users(id)
);

/* =========================
   6. SLOTS
   ========================= */
CREATE TABLE slots (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    physician_id BIGINT NOT NULL,
    location_id BIGINT NOT NULL,
    slot_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_available BOOLEAN DEFAULT TRUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,

    CONSTRAINT fk_slots_physician
        FOREIGN KEY (physician_id) REFERENCES physicians(id),

    CONSTRAINT fk_slots_location
        FOREIGN KEY (location_id) REFERENCES locations(id),

    UNIQUE (physician_id, location_id, slot_date, start_time)
);

/* =========================
   7. APPOINTMENT STATUS
   ========================= */
CREATE TABLE appointment_status (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(150),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL
);

/* Seed appointment status */
INSERT INTO appointment_status (code, description) VALUES
('BOOKED', 'Appointment booked'),
('CONFIRMED', 'Appointment confirmed'),
('CANCELLED', 'Appointment cancelled'),
('COMPLETED', 'Appointment completed'),
('NO_SHOW', 'Patient did not show');

/* =========================
   8. APPOINTMENTS
   ========================= */
CREATE TABLE appointments (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    patient_id BIGINT NOT NULL,
    physician_id BIGINT NOT NULL,
    location_id BIGINT NOT NULL,
    slot_id BIGINT NOT NULL,
    status_id BIGINT NOT NULL,
    booked_by BIGINT,
    notes TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,

    CONSTRAINT fk_appt_patient
        FOREIGN KEY (patient_id) REFERENCES patients(id),

    CONSTRAINT fk_appt_physician
        FOREIGN KEY (physician_id) REFERENCES physicians(id),

    CONSTRAINT fk_appt_location
        FOREIGN KEY (location_id) REFERENCES locations(id),

    CONSTRAINT fk_appt_slot
        FOREIGN KEY (slot_id) REFERENCES slots(id),

    CONSTRAINT fk_appt_status
        FOREIGN KEY (status_id) REFERENCES appointment_status(id),

    CONSTRAINT fk_appt_booked_by
        FOREIGN KEY (booked_by) REFERENCES users(id),

    UNIQUE (slot_id)
);

/* =========================
   9. APPOINTMENT LOGS
   ========================= */
CREATE TABLE appointment_logs (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    appointment_id BIGINT NOT NULL,
    previous_status_id BIGINT,
    new_status_id BIGINT NOT NULL,
    changed_by BIGINT,
    change_reason VARCHAR(255),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,

    CONSTRAINT fk_logs_appointment
        FOREIGN KEY (appointment_id) REFERENCES appointments(id),

    CONSTRAINT fk_logs_prev_status
        FOREIGN KEY (previous_status_id) REFERENCES appointment_status(id),

    CONSTRAINT fk_logs_new_status
        FOREIGN KEY (new_status_id) REFERENCES appointment_status(id),

    CONSTRAINT fk_logs_user
        FOREIGN KEY (changed_by) REFERENCES users(id)
);

SET FOREIGN_KEY_CHECKS = 1;
