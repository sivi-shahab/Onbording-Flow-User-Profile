-- 2.1 Flow versioning & branching
CREATE TABLE flow_versions (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name         VARCHAR NOT NULL,
  created_at   TIMESTAMP WITH TIME ZONE DEFAULT now(),
  is_active    BOOLEAN DEFAULT FALSE
);

CREATE TABLE questions (
  id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  flow_version_id UUID NOT NULL REFERENCES flow_versions(id),
  code           VARCHAR NOT NULL,
  text           TEXT NOT NULL,
  type           VARCHAR NOT NULL CHECK (type IN ('multiple_choice','text','number','date')),
  display_order  INTEGER NOT NULL
);

CREATE TABLE question_options (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  question_id UUID NOT NULL REFERENCES questions(id),
  code        VARCHAR NOT NULL,
  text        TEXT NOT NULL
);

CREATE TABLE flow_rules (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  flow_version_id  UUID NOT NULL REFERENCES flow_versions(id),
  question_id      UUID NOT NULL REFERENCES questions(id),
  option_id        UUID NOT NULL REFERENCES question_options(id),
  next_question_id UUID NOT NULL REFERENCES questions(id)
);

-- 2.2 Users & answers
CREATE TABLE users (
  id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email       VARCHAR UNIQUE NOT NULL,
  created_at  TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TABLE user_answers (
  id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id            UUID NOT NULL REFERENCES users(id),
  question_id        UUID NOT NULL REFERENCES questions(id),
  selected_option_id UUID REFERENCES question_options(id),
  answer_text        TEXT,
  answer_number      NUMERIC,
  answered_at        TIMESTAMP WITH TIME ZONE DEFAULT now()
);

-- 2.3 Profile snapshots for history
CREATE TABLE user_profile_history (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id      UUID NOT NULL REFERENCES users(id),
  profile_data JSONB NOT NULL,
  valid_from   TIMESTAMP WITH TIME ZONE DEFAULT now(),
  valid_to     TIMESTAMP WITH TIME ZONE
);
